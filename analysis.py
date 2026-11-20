import pandas as pd


def 정제(df):
    df = df.copy()
    print("시작", len(df))

    # 점수가 비어 있는 행 삭제
    df = df.dropna(subset=["점수"])
    print("빈 칸 제거", len(df))

    # 중복 행 삭제
    df = df.drop_duplicates()
    print("중복 제거", len(df))

    # 반과 과목의 앞뒤 공백 제거
    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()
    print("공백 제거", len(df))

    # 점수가 0~100 범위를 벗어난 행 삭제
    df = df[(df["점수"] >= 0) & (df["점수"] <= 100)]
    print("범위 밖 제거", len(df))

    return df


df = pd.read_csv("scores_2026.csv")
df = 정제(df)

# 정제 후 반과 과목의 고유한 값을 확인한다.
print(sorted(df["반"].unique()))
print(sorted(df["과목"].unique()))

# 수학 과목 학생 수를 출력한다.
수학_인원수 = len(df[df["과목"] == "수학"])
print("수학만 남긴 인원수:", 수학_인원수)

# 1반이면서 90점 이상인 학생 수를 출력한다.
조건에_맞는_인원수 = len(df[(df["반"] == "1반") & (df["점수"] >= 90)])
print("1반 90점 이상 인원수:", 조건에_맞는_인원수)

# 반별 점수 평균을 계산한다.
반별_점수_평균 = df.groupby("반")["점수"].mean()
print(반별_점수_평균)

# 과목과 반별 점수 평균을 계산한다.
과목_반별_점수_평균 = df.groupby(["과목", "반"])["점수"].mean()
print(과목_반별_점수_평균)

print(df.groupby("반").size())              # 반 전체 인원수
print(df.groupby(["과목", "반"]).size())     # 과목별·반별 인원수

def 반별평균(df):
    표 = df.groupby("반")["점수"].agg(
        ["count", "mean", "median", "max"]
    ).round(2)
    print(표)
    return 표["mean"]

미니 = 정제(pd.read_csv("mini.csv"))
print(반별평균(미니))