import evergreen as green
import custom_states as states

if __name__ == '__main__':
    game = green.Game()

    test = states.TestState(game, None)
    game.add_state(test)

    game.run()
