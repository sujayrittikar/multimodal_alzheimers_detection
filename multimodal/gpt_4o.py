import base64
import pandas as pd
from openai import OpenAI
from pydantic import BaseModel
from sklearn.metrics import classification_report


OPENAI_API_KEY = ""
FEATURE_COLS = ["Image Data ID", "Age", "GENOTYPE", "CDGLOBAL", "CDRSB", "MMSCORE", "HMSCORE", "NPISCORE", "GDTOTAL"]


class MultilingualDataset(BaseModel):
    classification: str
    reasoning: str

def get_openai_client():
    return OpenAI(api_key=OPENAI_API_KEY)

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def get_prompt(clinical_data_dict):
    clinical_data_str = ""

    for key, value in clinical_data_dict.items():
        if value:
            clinical_data_str += f"{key}: {value}\n"

    prompt = f"""
        Given the image of a Saggital MRI scan below, and the clinical details of patient, classify whether the patient is AD/MCI/CN.

        Full forms of the classes are as follows:
        AD: Alzheimer's Disease
        MCI: Mild Cognitive Impairment
        CN: Cognitively Normal

        Also, provide the reasoning behind why you classified the patient into the class you chose using following template:
        '''
            - Image features:
            - Clinical details:
        '''

        The clinical details of the patient are as follows:
        '''
            {clinical_data_str}
        '''

        Rules for output:
        - Classification should be one of the following: AD, MCI, CN.
        - Reasoning should be provided in the template mentioned.
    """
    return prompt

def get_gpt_4o_response(base64_image, clinical_data_dict, openai_client=None):
    prompt = get_prompt(clinical_data_dict)

    if not openai_client:
        raise ValueError("OpenAI client is not provided.")

    completion = openai_client.beta.chat.completions.parse(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    { "type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        response_format=MultilingualDataset,
    )
    return completion.choices[0].message.parsed

def get_classification_outputs():
    openai_client = get_openai_client()
    # Biomarkers file
    df = pd.read_csv('ADNI1_Final_With_Biomarkers.csv')
    # Clinical features columns
    df = df[FEATURE_COLS]
    # Create a list of dictionaries
    data_list = df.to_dict(orient='records')
    results_list = []

    for data_dict in data_list:
        image_path = f"preprocessed_images_3\{data_dict['Image Data ID']}.png"
        base64_image = encode_image(image_path)
        clinical_data_dict = {
            key: value
            if pd.notna(value) else None
            for key, value in data_dict.items()
                if key != "Image Data ID"
        }
        response = get_gpt_4o_response(base64_image, clinical_data_dict, openai_client)
        result_dict = {
            "Image Data ID": data_dict["Image Data ID"],
            "Classification": response.classification,
            "Reasoning": response.reasoning,
        }
        results_list.append(result_dict)
        print(f"Done for Image Data ID: {data_dict['Image Data ID']}")

    results_df = pd.DataFrame(results_list)
    return results_df

def evaluate_gpt_responses():
    df = pd.read_csv('ADNI1_Final_With_Biomarkers.csv')
    # Create a dict image id: group
    id_group_dict = dict(zip(df['Image Data ID'], df['Group']))

    gpt_results_df = pd.read_csv("gpt_4o_mini_classification_outputs.csv")
    # Predicted results dict
    results_dict = dict(zip(gpt_results_df['Image Data ID'], gpt_results_df['Classification']))

    # Sort the results by Image Data ID id_group_dict and results_dict
    id_group_dict = dict(sorted(id_group_dict.items()))
    results_dict = dict(sorted(results_dict.items()))

    # Create a list of real labels and predicted labels
    real_labels = list(id_group_dict.values())
    predicted_labels = list(results_dict.values())

    # classification report
    print(classification_report(real_labels, predicted_labels))


if __name__ == "__main__":
    # results_df = get_classification_outputs()
    # results_df.to_csv("gpt_4o_mini_classification_outputs.csv", index=False)
    evaluate_gpt_responses()
