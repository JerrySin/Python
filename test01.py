import pandas as pd

def test_run():
    df = pd.read_csv("Crypto_Resources.csv",delimiter=",")
    print(df) #print entire dataframe, python3


if __name__ == "__main__":
    test_run()
