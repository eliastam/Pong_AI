7# Author(s): your names here
# McGill ID(s): your IDs here
# Assignment 3, Question 4

hist_x = []
hist_y = []
class PongAI:
    
    def __init__(self, table_size):
        """
        table_size --   A tuple representing the dimensions of the table.
                        The x and y dimensions of the table are represented by
                                    table_size[0], table_size[1]
                        respectively.
        """
        self.table_size = table_size

    def pong_ai(self, paddle_rect, other_paddle_rect, ball_rect):
        """Return "up" or "down", depending on which way the paddle should go to
        align its centre with the centre of the ball
   
        Keyword arguments:
        paddle_rect -- A rectangle object representing the coordinates of your paddle.
                       The top-left corner of the rectangle is represented by the tuple
                                    paddle_rect.pos[0], paddle_rect.pos[1]
                       The dimensions (width, height) of the paddle are represented by
                                    paddle_rect.size[0], paddle_rect.size[1]
    
        other_paddle_rect -- A rectangle representing the opponent's paddle.
                        It is the same kind of object as above and its attributes
                        can be accessed in the same manner described above.
   
        ball_rect --    A rectangle representing the ball. It is the same kind of object
                        as the two above.
   
        Coordinates start at (0, 0) in the top-left corner.
        They look as follows:
   
   
                0             x
                |------------->
                |
                |             
                |
            y   v
        """          
     
        hist_x.append(ball_rect.pos[0])
        hist_y.append(ball_rect.pos[1])
        if paddle_rect.pos[0] > 200 : #playing from right
            if len(hist_x) < 2 :   #if we don't have enough information act like chaser until we have information
                if paddle_rect.pos[1]+paddle_rect.size[1]/2 < ball_rect.pos[1]+ball_rect.size[1]/2:
                    return "down" # move paddle down
                else: # paddle's y-coordinate must be below the ball's y-coordinate
                    return "up" # move paddle up
            else : 
                if (hist_x[len(hist_x)-2] - hist_x[len(hist_x)-1]) != 0 : #to make sure we're not dividing over 0
                    slope = (hist_x[len(hist_y)-2] - hist_x[len(hist_y)-1]) / (hist_x[len(hist_x)-2] - hist_x[len(hist_x)-1])
                    #calculate the slope m = (y1-y0)/ (x1-x0)  
                else:
                    slope = 0.99 #standard slope of 1 

                expected_x = 0 #initialize expected x
                expected_y = 0 #initialize expected x
                if slope > 0 :
                    expected_x = -1*ball_rect.pos[1]/ slope + ball_rect.pos[0] #caculate the expected x position when it bumps to the upper wall
                    expected_y = 0
                else : 
                    expected_x = (280 -ball_rect.pos[1])/ slope + ball_rect.pos[0] #caculate the expected x position when it bumps to the lower wall
                    expected_y = 280

                if hist_x[len(hist_x)-2] - hist_x[len(hist_x)-1] > 0 : # going away from our player Amaizing we're safe let's move to the middle
                    if paddle_rect.pos[1]+paddle_rect.size[1]/2 < 140:
                        return "down" # move paddle down
                    else: # paddle's y-coordinate must be below the ball's y-coordinate
                        return "up" # move paddle up
                else : 
                    if expected_x <=220:
                        if paddle_rect.pos[1]+paddle_rect.size[1]/2 < ball_rect.pos[1]+ball_rect.size[1]/2:
                            return "down" # move paddle down
                        else: # paddle's y-coordinate must be below the ball's y-coordinate
                            return "up" # move paddle up
                    elif expected_x > 350 and expected_x < 400 and abs(slope) > 1 and expected_y ==0:

                            if paddle_rect.pos[1]+paddle_rect.size[1]/2 < 70:
                                return "down" # move paddle down
                            else: # paddle's y-coordinate must be below the ball's y-coordinate
                                return "up" # move paddle up

                    elif expected_x > 350 and expected_x < 400 and abs(slope) > 1 and expected_y == 280:

                            if paddle_rect.pos[1]+paddle_rect.size[1]/2 > 210:
                                return "down" # move paddle down
                            else: # paddle's y-coordinate must be below the ball's y-coordinate
                                return "up" # move paddle up

                    else :
                        if ball_rect.pos[0] < 220 :
                            if paddle_rect.pos[1]+paddle_rect.size[1]/2 < 140:
                                return "down" # move paddle down
                            else: # paddle's y-coordinate must be below the ball's y-coordinate
                                return "up" # move paddle up
                        else:
                            if paddle_rect.pos[1]+paddle_rect.size[1]/2 < ball_rect.pos[1]+ball_rect.size[1]/2:
                                return "down" # move paddle down
                            else: # paddle's y-coordinate must be below the ball's y-coordinate
                                return "up" # move paddle up
        else: # left player
            #similar method with different numbers
            #so I didn't repeat the comments 
            if (hist_x[len(hist_x)-2] - hist_x[len(hist_x)-1]) != 0 :
                slope = (hist_x[len(hist_y)-2] - hist_x[len(hist_y)-1]) / (hist_x[len(hist_x)-2] - hist_x[len(hist_x)-1])
            else:
                slope = 0.99

            expected_x = 0
            expected_y = 0
            if slope < 0 :
                expected_x = -1*ball_rect.pos[1]/ slope + ball_rect.pos[0]
                expected_y = 0
            else : 
                expected_x = (280 -ball_rect.pos[1])/ slope + ball_rect.pos[0]
                expected_y = 280

            if hist_x[len(hist_x)-2] - hist_x[len(hist_x)-1] < 0 : # going away from our player Amaizing we're safe let's move to the middle
                if paddle_rect.pos[1]+paddle_rect.size[1]/2 < 140:
                    return "down" # move paddle down
                else: # paddle's y-coordinate must be below the ball's y-coordinate
                    return "up" # move paddle up
            else : 
                if expected_x > 220:
                    if paddle_rect.pos[1]+paddle_rect.size[1]/2 < ball_rect.pos[1]+ball_rect.size[1]/2:
                        return "down" # move paddle down
                    else: # paddle's y-coordinate must be below the ball's y-coordinate
                        return "up" # move paddle up
                elif expected_x >20 and expected_x < 100 and abs(slope) > 1 and expected_y ==0:

                        if paddle_rect.pos[1]+paddle_rect.size[1]/2 < 70:
                            return "down" # move paddle down
                        else: # paddle's y-coordinate must be below the ball's y-coordinate
                            return "up" # move paddle up

                elif expected_x > 20 and expected_x < 100 and abs(slope) > 1 and expected_y == 280:

                        if paddle_rect.pos[1]+paddle_rect.size[1]/2 > 210:
                            return "down" # move paddle down
                        else: # paddle's y-coordinate must be below the ball's y-coordinate
                            return "up" # move paddle up

                else :
                    if ball_rect.pos[0] > 220 :
                        if paddle_rect.pos[1]+paddle_rect.size[1]/2 < 140:
                            return "down" # move paddle down
                        else: # paddle's y-coordinate must be below the ball's y-coordinate
                            return "up" # move paddle up
                    else:
                        if paddle_rect.pos[1]+paddle_rect.size[1]/2 < ball_rect.pos[1]+ball_rect.size[1]/2:
                            return "down" # move paddle down
                        else: # paddle's y-coordinate must be below the ball's y-coordinate
                            return "up" # move paddle u