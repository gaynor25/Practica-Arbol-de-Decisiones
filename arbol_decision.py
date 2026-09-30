from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

wine = load_wine()

#'x' informacion de los vinos y 'y' como la respuesta que el arbol identificara
x = wine.data
y = wine.target

x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
    x, y, test_size=0.20, random_state=42
)

tree = DecisionTreeClassifier(max_depth=None, random_state=42)

tree.fit(x_entrenamiento, y_entrenamiento)

precision = tree.score(x_prueba, y_prueba)

print("Precisión del modelo:", precision)

rules = export_text(tree, feature_names=wine.feature_names)

print("\nReglas del árbol:")
print(rules)
