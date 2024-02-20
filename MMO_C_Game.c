///================================== MMO Project ==================================///

/// this project was made by Karl Jubénot 
/// the goal of this project is to learn C structure and to play with it
/// I created a an MMO project with several structure
/// Enjoy :)
#include <stdio.h>

typedef struct {                                                // This first structure represents the character positions on the game table
    int x;                                                      // The x value (abscissa) is an integer
    int y;                                                      // The y value (ordonate) is an integer
    int speed;                                                  // The speed value represents the character's speed, and it's an integer
} Player, Ennemis;                                              // All those values are link to the Player and the Enemies

typedef struct {                                                // This first structure represents the character spec
    int Damage;                                                 // The Damage value is an integer
    int Health;                                                 // The Health value is an integer
    int Armor;                                                  // The Armor value is an integer
} Spec;                                                         // I linked all those value to Spec

void movePlayer(Player* player, int dx, int dy) {               // I created a 'movePlayer' function in which i will use the Player values
                                                                // In my declaration I take dx value and dy value as integer 
    player->x += dx;                                            // I put the dx value in x (x is an Player value in the structure)
    player->y += dy;                                            // I put the dy value in y (y is an Player value in the structure)
}

int main() {                                                    // I will make the most important things in my main function
    Player player;                                              // I call my Player structure here 
    player.x = 0;                                               // Then I can call my x value (x is an Player value in the structure), and I put the x value to 0
    player.y = 0;                                               // Then I can call my x value (y is an Player value in the structure), and I put the y value to 0
    player.speed = 5;                                           // Then I can call my speed value (speed is an Player value in the structure), and I put the speed value to 5

    char input;                                                 // I creat an input value and it is a char
    int running = 1;                                            // I creat the running value and it is an integer
    int starter = 0;                                            // I creat the starter value and it is an integer

    while (running) {                                           // This condition while the game is start 
        if (starter == 0) {
            printf("Enter a command \n 1 : to chose Archer \n 2 : to chose Wizard \n 3 : to chose Knight \n 4 : to chose Ninja \n press 'q' to leave \n put your choice :\n");
            scanf(" %c", &input);

            if (input == '1') {
                printf("you chose Archer class\n");
                Spec Archer;
                Archer.Damage = 200;
                Archer.Health = 90;
                Archer.Armor = 50;
                starter = 1;
            } else if (input == '2') {
                printf("you chose Wizard class\n");
                Spec Wizard;
                Wizard.Damage = 130;
                Wizard.Health = 120;
                Wizard.Armor = 50;
                starter = 1;
            } else if (input == '3') {
                printf("you chose Knight class\n");
                Spec Knight;
                Knight.Damage = 80;
                Knight.Health = 110;
                Knight.Armor = 200;
                starter = 1;
            } else if (input == '4') {
                printf("you chose Ninja class\n");
                Spec Ninja;
                Ninja.Damage = 150;
                Ninja.Health = 90;
                Ninja.Armor = 80;
                starter = 1;
            } else if (input == 'q') {
                running = 0;
            }
        } else if (starter == 1) {
            printf("Enter a command (w/a/s/d to move, q to quit): ");
            scanf(" %c", &input);
            switch (input) {
                case 'w':
                    movePlayer(&player, 0, -player.speed);
                    break;
                case 'a':
                    movePlayer(&player, -player.speed, 0);
                    break;
                case 's':
                    movePlayer(&player, 0, player.speed);
                    break;
                case 'd':
                    movePlayer(&player, player.speed, 0);
                    break;
                case 'q':
                    running = 0;
                    break;
                default:
                    printf("Invalid command\n");
            }

            printf("Player position: x=%d, y=%d\n", player.x, player.y);
        }
    }

    return 0;
}
