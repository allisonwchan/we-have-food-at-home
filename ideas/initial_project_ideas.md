# Project Ideas

1. <b>EV charging station finder</b> <u>(most preferred!)</u>
   * Help EV owners plan out road trips or just a day's activities, find nearby charging stations in case they're running low on battery
   * Functionality: get charging stations near a user
     * User enters their coordinates and max distance, and gets list of stations within that distance
     * Each list item would include distance from user's coordinates, address, charger power, etc.
   * Possible API: [Open Charge Map](https://openchargemap.org/site/develop/api?ref=apilist.fun#/)
2. <b>Solar power map</b>
   * Help a user (like a homeowner, city engineer, etc.) determine if installing solar panel is worth it in a certain location
   * Functionality: get max solar eletricity that can be generated at a user's location
     * User enters their coordinates and gets max electricity a solar panel can produce
     * API response includes solar panel angle, surface area, type of technology used in solar panel, etc.
   * Possible API: [Open Weather Map](https://openweathermap.org/api/solar-panels-and-energy-prediction#get_all_panels)
3. <b>Recipe finder</b>
   * Help user finish up any leftover foods, try new foods
   * Functionality: get recipe(s) based on what items a user has
     * User enters at least 1 ingredient, filters by dietary restrictions, and gets a list of recipes
     * Each list item would include recipe name, ingredients and instructions, what ingredients user is missing (if any), etc.  
   * Possible API: [Spponacular](https://spoonacular.com/food-api)