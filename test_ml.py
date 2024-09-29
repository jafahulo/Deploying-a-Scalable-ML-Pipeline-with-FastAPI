import pytest
from sklearn.linear_model import LogisticRegression
import os
import pandas as pd
from ml.model import save_model, load_model

# TODO: add necessary import

@pytest.fixture
def model():
    """
    Fixture to provide a LogisticRegression model.
    """
    return LogisticRegression()
# TODO: implement the first test. Change the function name and input as needed
def test_model_type(model):
    """
    Tests if the returned model is of the correct type
    """
    assert isinstance(model, LogisticRegression)


# TODO: implement the second test. Change the function name and input as needed
def test_data_loads():
    """
    Checks if data loads from our csv file and contains at least 1 row.
    """
    project_path = "./"
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)

    assert data is not None
    assert data.shape[0] > 0


# TODO: implement the third test. Change the function name and input as needed
def test_save_model():
    """
    Test that we can save the model
    """
    save_model("Test value", "./test_model.pkl")
    assert os.path.exists("./test_model.pkl"), "Model file was not saved."
    os.remove("./test_model.pkl")

def test_load_model():
    """
    Test that we can load the model
    """
    save_model("Test value", "./test_model.pkl")
    assert os.path.exists("./test_model.pkl"), "Model file does not exist."

    model = load_model("./test_model.pkl")

    assert model == "Test value", "Model should not be none after loading."
    os.remove("./test_model.pkl")
