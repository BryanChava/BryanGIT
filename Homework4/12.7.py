#BRYAN CHAVARRIA
#1657040

def get_age():
    age = int(input())
    if 18 <= age <= 75:
        return age
    raise ValueError("Invalid age.")


def fat_burning_heart_rate(age):
    return (220 - age) * 0.7


if __name__ == "__main__":
    try:
        age = get_age()
        print("Fat burning heart rate for a", age, "year-old:", fat_burning_heart_rate(age), "bpm")
    except ValueError as e:
        print(e)
        print("Could not calculate heart rate info.\n")
