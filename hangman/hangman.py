import pygame
import os
import random

pygame.init()


WIDTH, HEIGHT = 800, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

CLOCK = pygame.time.Clock()
FPS = 60

FONT = pygame.font.Font(None, 36)


pygame.display.set_caption("Hangman UCC")


def load_images():
    LIFES = 7
    LIFES_LEFT = 6
    IMAGE_LIST = []
    for i in range(7):
        images = pygame.image.load(os.path.join('images', f'hangman{i}.png'))
        IMAGE_LIST.append(images)

    return LIFES, LIFES_LEFT, IMAGE_LIST


def load_button():
    BUTTON_LYST = []
    BUTTON_NAMES = ["A", "B", "C", "D"]
    for i in range(4):
        button_rect = pygame.Rect((i*100)+200, 400, 80, 40)
        BUTTON_LYST.append(button_rect)

    return BUTTON_LYST, BUTTON_NAMES


def draw_button(button_lyst, button_name_lyst):
    for button, button_name in zip(button_lyst, button_name_lyst):
        pygame.draw.rect(WINDOW, 'gray', button)
        name_surface = FONT.render(button_name, True, 'black')
        WINDOW.blit(name_surface, (button.x+30, button.y+13))


def get_rand(questions_dict):
    rand_key = random.choice(list(questions_dict.keys()))
    return rand_key, questions_dict[rand_key][1][0]


def display_question(questions_dict, current_question):
    question_surface = FONT.render(current_question, True, 'black')
    WINDOW.blit(question_surface, (300, 150))

    answer_pool = questions_dict[current_question][0]
    options = ['A', 'B', 'C', 'D']

    for i, answer in enumerate(answer_pool):
        option_text = f"{options[i]}: {answer}"
        answer_surface = FONT.render(option_text, True, 'black')
        # Adjust the Y position for each answer
        WINDOW.blit(answer_surface, (300, 200 + 40 * i))


def main():
    runnig = True

    questions_dict = {
        'What is the capital of France?': [['Paris', 'Berlin', 'London', 'Madrid'], ['A']],
        'Which planet is known as the Red Planet?': [['Venus', 'Saturn', 'Mars', 'Jupiter'], ['C']],
        'Who wrote "Romeo and Juliet"?': [['William Shakespeare', 'Charles Dickens', 'Jane Austen', 'Mark Twain'], ['A']],
        'What is the largest mammal in the world?': [['Elephant', 'Blue Whale', 'Giraffe', 'Rhino'], ['B']],
        'What is the chemical symbol for water?': [['H2O', 'O2', 'CO2', 'NaCl'], ['A']],
    }

    lifes, lifes_left, image_lyst = load_images()
    button_lyst, button_name_lyst = load_button()

    current_question = ""
    current_answer = ""
    time_for_new_question = True

    while runnig:
        CLOCK.tick(FPS)
        WINDOW.fill((255, 255, 255))
        WINDOW.blit(image_lyst[lifes-lifes_left], (50, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.time.delay(1000)
                runnig = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for index, button in enumerate(button_lyst):
                    if button.collidepoint(pos):
                        print("CLICKED", button_name_lyst[index])
                        if button_name_lyst[index] == current_answer:
                            time_for_new_question = True
                        else:
                            lifes_left -= 1

        if time_for_new_question:
            current_question, current_answer = get_rand(questions_dict)
            print(current_question, current_answer)
            time_for_new_question = False

        display_question(questions_dict, current_question)

        if lifes_left == 0:
            runnig = False

        draw_button(button_lyst, button_name_lyst)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
