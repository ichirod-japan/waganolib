from wagano import calculation

def test_haversine():
    assert calculation.haversine(52.370216, 4.895168, 52.520008,
    13.404954) == 945793.4375088713