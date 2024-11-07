# OO code using turtle graphics
- From the starting code, polygon_art.py, you are to write an OO program that generates different pieces of art works
- Fork, then, clone this repo
- Read the instructions given in the course's Google Classroom and start coding
- Once you are done, push your final code to your Github repo and modify this README to report on the work you have done

- This is what a had done in this work.
- I didn't make exact style from your given template but i do using the same class.
- class Polygon
    - First i make class Polygon, and make whenever you make a var by using this class it will randomly give its
      attribute such as num_side, size, orientation, location and border_size but color i just give it white color first.
    - also make getter and setter for all of them.
    - and the random color function stay the same.
    - and the draw_polygon function stay almost the same except the only input is (self) and
      the inside using self._xxx instead.
- class EmbeddedPolygon(Polygon)
    - it does the same as __init__ polygon but have additional of rep_time and reduction_ratio
    - rep_time is use to make an inside polygon with samller size
    - reduction_ratio is self explaintory
    - the function has resemblance of the polygon one except
      - it draw the polygon {self._rep_time} times.
      - the size was reduced by init_size * (reduction_ratio ** i) .; i is times from for loop.
      - i didnt do moveto function but it exist in draw_polygon
      - this function have the same input as non-embedded one.
- class Run
    - by running the __init__ function it will ask for input number.
    - if the number is not 1-9 it will ValueError.
    - and runing choice function that will indicates how the polygon will be drawn.
    - in the choice i set for loop for how many times polygon will be drawn.
    - in every loop it will generate new self.x which was random.
    - in loop also have random color function and the modifiers run by choice before drawing it.
- main code
    - using run class.
    - set blackground to black
    - run the choice
    - turtle.done
