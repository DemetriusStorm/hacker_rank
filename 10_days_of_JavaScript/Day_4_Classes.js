/*
Create a Polygon class that has the following properties:

A constructor that takes an array of integer values describing the lengths of the polygon's sides.
A perimeter() method that returns the polygon's perimeter.
Locked code in the editor tests the Polygon constructor and the perimeter method.
*/


class Polygon {
  constructor(array) {
    this.array = array;
    this.partiesTotal = 0;
  }

  perimeter() {

    for (let n of this.array) {
      this.partiesTotal += n;
    }
    return this.partiesTotal;
  };

};


// Create a polygon with side lengths 3, 4, and 5
let triangle = new Polygon([3, 4, 5]);

// Print the perimeter
console.log(triangle.perimeter());
