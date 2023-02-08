/*
'''
Ned and Mary want to choose a restaurant to bring their kids to for the evening, and they both have a list of their favorite places, represented by strings and sorted by preference. The place they each prefer the most is at the beginning of the list, and their least preferred at the end.

You need to help them find the optimal match to dine at based on their combined preferences score. They will often have to compromise, so their ideal option is a place they both have on their list, and it has the highest combined preference score.

To calculate the highest combined preference score, get the restaurant with the minimum index sum when adding the indices of the restaurant on both of their lists together. If multiple restaurants have the same highest score, output all of them.
 

EXAMPLE(S)
Input:
nedsChoices = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
marysChoices = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Input:
nedsChoices = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
marysChoices = ["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: They both have "Shogun" on their preferred list and it has the highest preference score with an index sum of 1 (0+1). They both listed "KFC" but it has a lower preference score because the index sum is 3 (0+3). Likewise, "Burger King" has a preference score of 4 (2+2).

Input:
nedsChoices = ["Guppy House", "In-n-Out", "Dairy Queen"]
marysChoices = ["In-n-Out", "Guppy House", "Dairy Queen"]
Output: ["Guppy House", "In-n-Out"]
Explanation: They both have "Guppy House" and "In-n-Out" on their preferred list and both restaurants have the same highest total preference score with an index sum of 1 (0+1 and 1+0). They both listed "Dairy Queen" but the preference score is 4 (2+2).
 

FUNCTION SIGNATURE
function findCompatibleRestaurantsBetween(ned, mary) {
def findCompatibleRestaurantsBetween(ned: list[str], mary: list[str]) -> list[str]:
'''
*/

// Notes:
// Find the common restaurants
// Maintain a hash map, where the restaurant is the key and position is the value

// For each element in first array, find element in the second array
// 1. Use array search
// 2. Use hash map

// What about multiple restaurants?
// Use hash map that maps from preference score to restaurants

// Solution:
// Hash map from restaurant name to index (for Ned)
// Iterate through Mary's choices and look in Ned's hash map
// Create result array
// Every time new minimum, clean out array; every time same score,
// add to array

function findCompatibleRestaurantsBetween(ned, mary) {
    const mem = {};
    let result = [];
    let minScore = Infinity;
  
    // O(n)
    for (let i = 0; i < ned.length; i++) mem[ned[i]] = i;
  
    // O(m)
    for (let i = 0; i < mary.length; i++) {
      if (mary[i] in mem) { // O(1)
        if (mem[mary[i]] + i < minScore) { // O(1)
          result = [mary[i]];
          minScore = i + mem[mary[i]]
        }
        else if (mem[mary[i]] + i === minScore) { // O(1)
          result.push(mary[i]); // O(1)
        }
      }
    }
  
    return result;
  }
  let nedsChoices = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
  let marysChoices = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
  console.log(findCompatibleRestaurantsBetween(nedsChoices,marysChoices))
  
  let nedsChoices1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
  let marysChoices1 = ["KFC", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
  console.log(findCompatibleRestaurantsBetween(nedsChoices1,marysChoices1))
  
  nedsChoices1 = [], marysChoices1 = []
  console.log(findCompatibleRestaurantsBetween(nedsChoices1,marysChoices1))
  
  let nedsChoices4 = ["Tapioca Express", "Burger King", "KFCC"]
  let marysChoices4 = ["KFC", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse"]
  console.log(findCompatibleRestaurantsBetween(nedsChoices4,marysChoices4))
  
  nedsChoices = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
  marysChoices = ["KFC", "Burger King", "Tapioca Express", "Shogun"]
  
  console.log(findCompatibleRestaurantsBetween(nedsChoices,marysChoices))
  
  nedsChoices = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
  marysChoices = ["KFC", "Shogun", "Burger King"]
  console.log(findCompatibleRestaurantsBetween(nedsChoices,marysChoices)) // Output: ["Shogun"]
  
  // Time complexity?
  // O(n + m) 
  
  // Space complexity?
  // O(n) 