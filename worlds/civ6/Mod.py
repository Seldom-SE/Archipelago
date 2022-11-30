from worlds.AutoWorld import World

def generate_mod(world: World):
    checks = []
    emigrants = []
    scope = {
        "CHECKS": checks,
        "EMIGRANTS": emigrants,
    }
