/**
  The code in the editor has a tagged template literal that passes the area and perimeter of a rectangle to a tag function named sides. Recall that the first argument of a tag function is an array of string literals from the template, and the subsequent values are the template's respective expression values.

 * Determine the original side lengths and return an array:
 * - The first element is the length of the shorter side
 * - The second element is the length of the longer side
 *
 * Parameter(s):
 * literals: The tagged template literal's array of strings.
 * expressions: The tagged template literal's array of expression values (i.e., [area, perimeter]).
*/

const sides = (literals, ...expressions) => {
    const area = expressions[0];
    const perimeter = expressions[1];

    const s1 = (perimeter + Math.sqrt(perimeter ** 2 - 16 * area)) / 4;
    const s2 = (perimeter - Math.sqrt(perimeter ** 2 - 16 * area)) / 4;

    return [s1, s2].sort();
};

console.log(sides`The area is: ${140}.\nThe perimeter is: ${48}.`);
