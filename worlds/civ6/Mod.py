from worlds.AutoWorld import World

def generate_mod(world: World, output_dir: str):
    checks = []

    for location in world.multiworld.get_filled_locations(world.player):
        checks.append({
            "VALILLA": "",
            "TECH": "",
            "TYPE": "",
            "DESC": "",
            "POS_TYPE": "",
            "SRC_TYPE": "", # Optional
        })

    emigrants = []

    emigrants.append({
        "TECH": "",
        "TYPE": "",
    })

    scope = {
        "CHECKS": checks,
        "EMIGRANTS": emigrants,
    }
