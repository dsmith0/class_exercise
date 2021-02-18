def test_coordinates():
	from two_tuples import coordinates
	answer = coordinates(2, 2, 6, 6,)
	expected = 4
	assert answer == expected


def test_coordinates():
	from two_tuples import coordinates
	answer = coordinates(-2, 0, -6, 4)
	expected = 2
	assert answer == expected