from app.interface_connector import get_recommendations

models = ['minilm', 'scibert', 'specter']

titles = ['Lattice QCD predictions for shapes of event distributions along the freezeout curve in heavy-ion collisions', 'SUSY Searches at LEP', 'The impact of air transport availability on research collaboration: A case study of four universities']
for title in titles:
    for model in models:
        print(f"Testing '{model}' model for title: {title}")
        results = get_recommendations(title, model, top_k=5)
        if results:
            for res in results:
                print(f"- {res['title']} (Similarity: {res['similarity']})")
        else:
            print(f"No results found for '{title}' using '{model}'")
        print("-" * 80)
    print("=" * 80)
print("All title tests completed.")
print("=" * 80)


keywords = ['Lattice QCD', 'SUSY', 'air transport', 'machine learning, biology', 'machine learning biology', 'fewiucawoxoiaio']
for keyword in keywords:
    for model in models:
        print(f"Testing '{model}' model for keyword: {keyword}")
        results = get_recommendations(keyword, model, top_k=5)
        if results:
            for res in results:
                print(f"- {res['title']} (Similarity: {res['similarity']})")
        else:
            print(f"No results found for '{keyword}' using '{model}'")
        print("-" * 80)
    print("=" * 80)
print("All keyword tests completed.")