import pygame


class SpriteSheets():
    def __init__(self, filename, rows, colomns, scale):
        self.sheet = pygame.image.load(filename).convert_alpha()
        self.sheet = pygame.transform.scale(self.sheet, (scale))


        self.rows = rows
        self.colomns = colomns
        self.total_cells = rows * colomns

        self.rect = self.sheet.get_rect()
        self.cell_width = self.rect.width / colomns
        self.cell_height = self.rect.height / rows
        
    def get_sheet_frame(self):
        frames =[]
        for row in range(self.rows):
            for column in range(self.colomns):
                area = (self.rect.left  +  self.cell_width * column, self.rect.top + self.cell_height * row)
                frames.append(self.sheet.subsurface(pygame.Rect(area,(self.cell_width, self.cell_height))))
        
        return frames
