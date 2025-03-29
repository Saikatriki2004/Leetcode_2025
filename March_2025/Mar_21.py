from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Convert to sets for O(1) lookup
        recipe_set = set(recipes)
        supply_set = set(supplies)
        
        # Map recipes to their ingredients
        ingredient_dict = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        
        # Check eligibility: all non-recipe ingredients must be in supplies
        eligible = {}
        for recipe in recipes:
            # For each ingredient not in recipe_set, it must be in supply_set
            all_non_recipe_available = all(
                ing in supply_set for ing in ingredient_dict[recipe] if ing not in recipe_set
            )
            eligible[recipe] = all_non_recipe_available
        
        # Build dependency graph and indegree
        dependency_graph = defaultdict(list)
        indegree = {recipe: 0 for recipe in recipes}
        
        for recipe in recipes:
            for ing in ingredient_dict[recipe]:
                if ing in recipe_set:
                    # If ingredient is a recipe, add an edge from it to the current recipe
                    dependency_graph[ing].append(recipe)
                    indegree[recipe] += 1
        
        # Initialize queue with recipes that have no recipe dependencies and are eligible
        queue = deque([
            recipe for recipe in recipes 
            if indegree[recipe] == 0 and eligible[recipe]
        ])
        made_recipes = []
        
        # BFS to process all makeable recipes
        while queue:
            recipe = queue.popleft()
            made_recipes.append(recipe)
            # Update dependent recipes
            for dependent in dependency_graph[recipe]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0 and eligible[dependent]:
                    queue.append(dependent)
        
        return made_recipes
