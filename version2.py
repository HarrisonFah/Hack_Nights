# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 14:20:14 2019

@author: daniv
"""

import pygame

class Game:
    def __init__(self,surface):
        self.close_clicked = False
        self.continue_game = True
        self.game_clock = pygame.time.Clock()
        self.frame_rate = 60
        self.surface = surface
        self.background_color = pygame.Color('black')
   
        self.wall_1 = wall('orange',[450, 150],[20, 100], self.surface)
    
    def play(self):
        while self.close_clicked == False:
            self.update
            self.draw()
            self.handle_events()
            if self.continue_game == True:

                self.decide_continue
            self.game_clock.tick(self.frame_rate)
    
    def draw(self):
        # Draw all game objects
        self.surface.fill(self.background_color) #clear display surface first
        self.wall_1.draw()
        
        pygame.display.update() #displays updated surface
       
    def update(self):
        self.wall.apply_gravity()
        pass
    
    def decide_continue(self):
        pass

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.wall_1.move([0,20])   
        keys = pygame.key.get_pressed()  
        if keys [pygame.K_UP]:
            self.wall_1.move([0,-20])
        if keys [pygame.K_DOWN]:
            self.wall_1.move([0,20])
        if keys [pygame.K_LEFT]:
            self.wall_1.move([-20,0])
        if keys [pygame.K_RIGHT]:
            self.wall_1.move([20,0])
        else:
            self.wall_1.move([0,0])
            self.wall_1.apply_gravity()
                
class wall:
    def __init__(self, wall_colour, wall_position, wall_dimensions, surface):
        self.color = pygame.Color(wall_colour)
        self.position = wall_position
        self.dimensions = wall_dimensions
        self.wall = [wall_position, wall_dimensions]
        self.surface = surface
    def move(self, velocity):
        self.velocity = velocity 

        self.position[0] = self.position[0] + self.velocity[0]
        self.position[1] = self.position[1] + self.velocity[1]
        
        size = self.surface.get_size() # tuple (width, height)
        # check right index = 0, check bottom index = 1
        for index in range(0,2):
            if self.position[index] + self.dimensions[index] >= size[index]:
                self.position[index] = size[index] - self.dimensions[index]
        # check left index = 0, check bottom index = 1
        for index in range(0,2):
            if self.position[index] <= 0:
                self.position[index] = 0
        
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.wall)
    
    def apply_gravity(self):
        size = self.surface.get_size() # tuple (width, height)
        change_in_velocity = 0.50
        if self.velocity[1] == 0:
            self.move([0,19])
            self.velocity[1] += change_in_velocity
        # check if on ground
        if self.position[1] - self.dimensions[1] >= size[1]:
            #self.position[1] = size[1] - self.dimensions[1]
            self.velocity[1] = 0
        

def main():
    pygame.init()
    size = (800,600)
    title = 'practice'
    pygame.display.set_mode(size)
    pygame.display.set_caption(title)

    surface = pygame.display.get_surface()
    game = Game(surface)
    game.play()
    pygame.quit()
    
main()



