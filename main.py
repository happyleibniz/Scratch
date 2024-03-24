import Scratch.Scratch as Scratch

program = Scratch.Main
background = Scratch.Background(name="Background", background_images=['Scratch/assets/background.svg'])
a_sprite = Scratch.Sprite(name="Sprite1", sprite_images=["costume1.svg", "bowtie.svg"],direction=90,sounds=['snoring.wav'])
background.show()
a_sprite.show()
a_sprite.play()
a_sprite.next_costume()
a_sprite.change_x_by(50)
a_sprite.set_size_to(900)
a_sprite.update()
Scratch.stay()

