import pygame

# Inicialização do Pygame
pygame.init()

# Definição das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# Definição das fontes
font_name = pygame.font.match_font('arial')
font_score = pygame.font.SysFont(font_name, 900)
font_team = pygame.font.SysFont(font_name, 250)

# Definição das variáveis
team1_name = "Claro"
team2_name = "Escuro"
team1_score = 0
team2_score = 0
selected_team = 1

# Criação da janela
size = (1920, 1010)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Placar de Basquetebol")

# Função para desenhar o placar
def draw_score():
    screen.fill(BLACK)
    team1_text = font_team.render(team1_name, True, WHITE)
    team2_text = font_team.render(team2_name, True, GRAY)
    team1_score_text = font_score.render(str(team1_score), True, RED)
    team2_score_text = font_score.render(str(team2_score), True, RED)
    screen.blit(team1_text, (size[0] // 4 - team1_text.get_width() // 2, 50))
    screen.blit(team2_text, (3 * size[0] // 4 - team2_text.get_width() // 2, 50))
    screen.blit(team1_score_text, (size[0] // 4 - team1_score_text.get_width() // 2, 300))
    screen.blit(team2_score_text, (3 * size[0] // 4 - team2_score_text.get_width() // 2, 300))
    if selected_team == 1:
        screen.blit(font_team.render("*", True, WHITE), (size[0] // 4 - team1_text.get_width() // 2 - 50, 50))
    else:
        screen.blit(font_team.render("*", True, GRAY), (3 * size[0] // 4 - team2_text.get_width() // 2 - 50, 50))

# Loop principal do jogo
done = False
while not done:
    # Verificação de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if selected_team == 1:
                    team1_score += 1
                else:
                    team2_score += 1
            elif event.key == pygame.K_2:
                if selected_team == 1:
                    team1_score += 2
                else:
                    team2_score += 2
            elif event.key == pygame.K_3:
                if selected_team == 1:
                    team1_score += 3
                else:
                    team2_score += 3
            elif event.key == pygame.K_BACKSPACE:
                if selected_team == 1 and team1_score > 0:
                    team1_score -= 1
                elif selected_team == 2 and team2_score > 0:
                    team2_score -= 1
            elif event.key == pygame.K_TAB:
                selected_team = 2 if selected_team == 1 else 1
            elif event.key == pygame.K_F1:
                team1_score = team2_score = 0
    # Desenho do placar
    draw_score()
    # Atualização da tela
    pygame.display.flip()

# Encerramento do Pygame
pygame.quit()
