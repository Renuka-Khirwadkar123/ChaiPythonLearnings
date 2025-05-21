->Command to create virtual environment
python -m venv venv

-> Activate virtual enviornment
env\Scripts\activate

->Deactivate envioronment
type deactivate

->view packages in current envionment
pip list

->save dependencies in requirments.txt

pip freeze > requirements.txt

->how to use requirements.txt

1. Create environment
2. Activate environment

->tip: Create virtual environment folder to store environment related files. This will help to remove envirnment related data when not needed anymore

-> install dependencies from one enviornment to another environment
pip install -r requirements.txt



