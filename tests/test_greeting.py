from weather_app import greeting


def test_convert_to_fahr():
    temp_Cs = [-40, 0, 100]
    temp_Fs = [-40, 32, 212]

    for temp_C, temp_F in zip(temp_Cs, temp_Fs):
        assert greeting.convert_to_fahr(temp_C) == temp_F
