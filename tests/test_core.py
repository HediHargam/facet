def test_get_global_config():
    import yieldengine
    config = yieldengine.get_global_config()
    # yaml.safe_load() returns a list of items/dicts
    assert type(config) == list, "Expected a list"
