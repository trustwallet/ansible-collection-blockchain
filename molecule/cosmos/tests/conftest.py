import os

chain_name = os.environ['COSMOS_CHAIN_NAME']

def pytest_collection_modifyitems(items, config):
    """ deselect test items which do not match the fixture chain """
    deselection_items = []
    for item in items:
        chains = set([mark.args[0] for mark in item.iter_markers(name='chain')])
        if len(chains) > 0:
            if chain_name not in chains:
                deselection_items.append(item)
    items[:] = [item for item in items if item not in deselection_items]
    config.hook.pytest_deselected(items=deselection_items)
