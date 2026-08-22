import json

# Tree definitions with keys
father_tree = {
    "F0": ["F1_home", "F1_pub", "F1_travel"],
    "F1_home": ["F2_movie", "F2_book", "F2_rest"],
    "F1_pub": ["F2_beer_tasting", "F2_pub_games", "F2_sports_screening"],
    "F1_travel": ["F2_seaside", "F2_mountains", "F2_city"],
    "F2_movie": ["F3_movie_lore", "F3_popcorn_guy", "F3_critic"],
    "F2_book": ["F3_read_history", "F3_read_sci_book", "F3_read_novel"],
    "F2_rest": ["F3_couch_nap", "F3_garden_work", "F3_meditate"],
    "F2_beer_tasting": ["F3_order_ipa", "F3_order_lager", "F3_order_craft"],
    "F2_pub_games": ["F3_play_billiards", "F3_play_cards", "F3_deep_talk"],
    "F2_sports_screening": ["F3_watch_match", "F3_check_stats", "F3_cheer_team"],
    "F2_seaside": ["F3_sailing", "F3_deep_diving", "F3_swim_laps"],
    "F2_mountains": ["F3_heavy_hiking", "F3_rock_climbing", "F3_chop_wood"],
    "F2_city": ["F3_history_museum", "F3_architecture", "F3_rock_concert"]
}

mother_tree = {
    "M0": ["M1_home", "M1_entertainment", "M1_travel"],
    "M1_home": ["M2_movie", "M2_book", "M2_rest"],
    "M1_entertainment": ["M2_shopping", "M2_workshop", "M2_cafe_relax"],
    "M1_travel": ["M2_seaside", "M2_mountains", "M2_city"],
    "M2_movie": ["M3_movie_plot", "M3_emotional_scenes", "M3_enjoy_snacks"],
    "M2_book": ["M3_read_poetry", "M3_read_psychology", "M3_read_biography"],
    "M2_rest": ["M3_do_yoga", "M3_herbal_tea", "M3_bake_cookies"],
    "M2_shopping": ["M3_art_print_hunting", "M3_indie_perfume", "M3_vintage_finds"],
    "M2_workshop": ["M3_pottery_wheel", "M3_floral_design", "M3_pastry_baking"],
    "M2_cafe_relax": ["M3_botanical_patio", "M3_read_magazine", "M3_patio_espresso"],
    "M2_seaside": ["M3_sunbathing", "M3_seafood_dinner", "M3_beach_spa"],
    "M2_mountains": ["M3_nature_photography", "M3_alpine_resort", "M3_scenic_views"],
    "M2_city": ["M3_art_gallery", "M3_fashion_boutique", "M3_opera_theatre"]
}

son_tree = {
    "S0": ["S1_home", "S1_outdoors", "S1_travel"],
    "S1_home": ["S2_movie", "S2_book", "S2_rest"],
    "S1_outdoors": ["S2_arcade", "S2_park", "S2_walk"],
    "S1_travel": ["S2_seaside", "S2_mountains", "S2_city"],
    "S2_movie": ["S3_movie_effects", "S3_watch_cartoons", "S3_fall_asleep"],
    "S2_book": ["S3_read_comics", "S3_read_fantasy", "S3_read_manga"],
    "S2_rest": ["S3_play_video_games", "S3_build_lego", "S3_sleep_late"],
    "S2_arcade": ["S3_play_games", "S3_win_tickets", "S3_eat_pizza"],
    "S2_park": ["S3_ride_bmx", "S3_see_graffiti", "S3_skate_halfpipe"],
    "S2_walk": ["S3_ride_scooter", "S3_ride_bicycle", "S3_walk_the_dog"],
    "S2_seaside": ["S3_swimming", "S3_water_slides", "S3_sandcastles"],
    "S2_mountains": ["S3_sledding", "S3_camping", "S3_hiking"],
    "S2_city": ["S3_visit_toy_shop", "S3_visit_zoo", "S3_eat_fast_food"]
}

# cleaned keys for comparison
tag_map = {
    # 1
    "F1_home": "home", "F1_pub": "pub", "F1_travel": "travel",
    "M1_home": "home", "M1_entertainment": "pub", "M1_travel": "travel",
    "S1_home": "home", "S1_outdoors": "pub", "S1_travel": "travel",
    # 2
    "F2_movie": "movie", "F2_book": "book", "F2_rest": "rest",
    "F2_beer_tasting": "beer", "F2_pub_games": "friends", "F2_sports_screening": "walk",
    "F2_seaside": "seaside", "F2_mountains": "mountains", "F2_city": "city",
    
    "M2_movie": "movie", "M2_book": "book", "M2_rest": "rest",
    "M2_shopping": "beer", "M2_workshop": "friends", "M2_cafe_relax": "walk",
    "M2_seaside": "seaside", "M2_mountains": "mountains", "M2_city": "city",
    
    "S2_movie": "movie", "S2_book": "book", "S2_rest": "rest",
    "S2_arcade": "beer", "S2_park": "friends", "S2_walk": "walk",
    "S2_seaside": "seaside", "S2_mountains": "mountains", "S2_city": "city"
}

def get_tag(node_string):
    return tag_map.get(node_string, node_string.split("_")[1] if "_" in node_string else node_string)

def get_parent_node(child_node, tree):
    for parent, children in tree.items():
        if child_node in children:
            return parent
    return None

# JSON configuration and title
configuration = {
    "scenario": "Multi-Agent Layered Decision Tree via Maximum Entropy",
    "description": "A generated decision tree that simulates the behavior of agents through 4 levels of depth using clean semantic nodes.",
    "depth": 4,
    "branching_factor": 3,
    "agents": {"father": {}, "mother": {}, "son": {}},
    "conditional_probabilities": []
}

def convert_tree_to_nodes(tree, prefix):
    nodes_obj = {}
    for parent, children in tree.items():
        nodes_obj[parent] = {
            "text": f"Layer for {prefix} from {parent}.",
            "children": [{"next": child, "action": child.lower(), "prob": 1.0/len(children)} for child in children]
        }
    return nodes_obj

configuration["agents"]["father"] = convert_tree_to_nodes(father_tree, "father")
configuration["agents"]["mother"] = convert_tree_to_nodes(mother_tree, "mother")
configuration["agents"]["son"] = convert_tree_to_nodes(son_tree, "son")

conditionals = []

# Lists over levels
all_f1 = father_tree["F0"]
all_m1 = mother_tree["M0"]
all_s1 = son_tree["S0"]

all_f2 = [item for sublist in [father_tree[k] for k in father_tree["F0"]] for item in sublist]
all_m2 = [item for sublist in [mother_tree[k] for k in mother_tree["M0"]] for item in sublist]
all_s2 = [item for sublist in [son_tree[k] for k in son_tree["S0"]] for item in sublist]

all_f3 = []
for k in father_tree:
    if k != "F0" and k not in father_tree["F0"]:
        all_f3.extend(father_tree[k])

all_m3 = []
for k in mother_tree:
    if k != "M0" and k not in mother_tree["M0"]:
        all_m3.extend(mother_tree[k])

# LEVEL 1 - Macro ambient
for f1 in all_f1:
    f1_tag = get_tag(f1)
    
    # Father - Mother
    conditionals.append({
        "condition": {"father": f1},
        "effects": {f"mother.{m1}": 0.8 if get_tag(m1) == f1_tag else 0.1 for m1 in all_m1}
    })
    
    # Father + Mother - Son
    for m1 in all_m1:
        m1_tag = get_tag(m1)
        parents_aligned = (f1_tag == m1_tag)
        
        effects_dict = {}
        for s1 in all_s1:
            if parents_aligned:
                effects_dict[f"son.{s1}"] = 0.9 if get_tag(s1) == f1_tag else 0.05
            else:
                effects_dict[f"son.{s1}"] = 1.0 / 3.0
                
        conditionals.append({
            "condition": {"father": f1, "mother": m1},
            "effects": effects_dict
        })

# LEVEL 2 - Activities
for f2 in all_f2:
    f2_parent = get_parent_node(f2, father_tree)
    f2_tag = get_tag(f2)
    
    # Father - Mother
    effects_dict_m = {}
    for m2 in all_m2:
        m2_parent = get_parent_node(m2, mother_tree)
        if get_tag(f2_parent) == get_tag(m2_parent) and get_tag(m2) == f2_tag:
            effects_dict_m[f"mother.{m2}"] = 0.8
        else:
            effects_dict_m[f"mother.{m2}"] = 0.2 / 8.0
            
    conditionals.append({
        "condition": {"father": f2},
        "effects": effects_dict_m
    })

    # Father + Mother - Son
    for m2 in all_m2:
        m2_tag = get_tag(m2)
        parents_aligned = (f2_tag == m2_tag)
        
        effects_dict_s = {}
        for s2 in all_s2:
            s2_tag = get_tag(s2)
            if parents_aligned:
                if s2_tag == f2_tag:
                    effects_dict_s[f"son.{s2}"] = 0.9
                else:
                    effects_dict_s[f"son.{s2}"] = 0.1 / 8.0
            else:
                effects_dict_s[f"son.{s2}"] = 1.0 / 9.0
                
        conditionals.append({
            "condition": {"father": f2, "mother": m2},
            "effects": effects_dict_s
        })

# LEVEL 3 - Final actions 
for f3 in all_f3:
    f3_parent = get_parent_node(f3, father_tree)
    f3_parent_tag = get_tag(f3_parent)
    
    for m3 in all_m3:
        m3_parent = get_parent_node(m3, mother_tree)
        m3_parent_tag = get_tag(m3_parent)
        
        parents_aligned = (f3_parent_tag == m3_parent_tag)
        effects_dict_s3 = {}
        
        all_s3_leaves = []
        for s2_key in son_tree:
            if s2_key != "S0" and s2_key not in son_tree["S0"]:
                all_s3_leaves.extend(son_tree[s2_key])
                
        for s3 in all_s3_leaves:
            s3_parent = get_parent_node(s3, son_tree)
            s3_parent_tag = get_tag(s3_parent)
            
            if parents_aligned:
                if s3_parent_tag == f3_parent_tag:
                    sub_branch = son_tree[s3_parent]
                    if s3 == sub_branch[0]: effects_dict_s3[f"son.{s3}"] = 0.45
                    elif s3 == sub_branch[1]: effects_dict_s3[f"son.{s3}"] = 0.40
                    elif s3 == sub_branch[2]: effects_dict_s3[f"son.{s3}"] = 0.15
                else:
                    effects_dict_s3[f"son.{s3}"] = 0.0
            else:
                effects_dict_s3[f"son.{s3}"] = 1.0 / 27.0
                    
        conditionals.append({
            "condition": {"father": f3, "mother": m3},
            "effects": effects_dict_s3
        })

configuration["conditional_probabilities"] = conditionals

output_file = "multi-agent/exhaustive_combinations_clean.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(configuration, f, indent=2, ensure_ascii=False)

print("=" * 60)
print(f"New dataset generated '{output_file}'!")
print(f"Total number of unique rules: {len(conditionals)}")
print("=" * 60)