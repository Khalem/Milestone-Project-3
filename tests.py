def test_username_stored(user, usernames):
    """ Test that user gets stored into usernames. Raise AssertionError
    if not. 
    """
    
    assert user in usernames, "Expected {0} to be stored in {1}, however it was not".format(user, usernames)
    
