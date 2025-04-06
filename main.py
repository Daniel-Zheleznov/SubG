import evergreen as green
import custom_states as states

if __name__ == '__main__':
    game = green.Game()

    fantasia_state = states.fantasia(game, None)
    game.add_state(fantasia_state)

    game.run()
