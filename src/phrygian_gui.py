from PyQt5.QtWidgets import (
  QApplication, QWidget, 
  QPushButton, QVBoxLayout, 
  QHBoxLayout, QDialog, 
  QLabel, QFileDialog, 
  QTextEdit, QComboBox, 
  QFormLayout, QLineEdit, 
  QGridLayout, QTextBrowser,
  QLayout, QSpinBox
)
from PyQt5.QtCore import Qt
from css import PHRYGIAN_GUI

# from process_midis import process
# from train_network import train
# from generate_music import generate
from music21 import instrument

PROCESS_STRING = 'Process MIDIs melodies'
TRAIN_STRING = 'Train neuronal network'
GENERATE_STRING = 'Generate music'

INSTRUMENTS = {
    "Accordion": instrument.Accordion(),
    "AcousticBass": instrument.AcousticBass(),
    "AcousticGuitar": instrument.AcousticGuitar(),
    "Agogo": instrument.Agogo(),
    "Alto": instrument.Alto(),
    "AltoSaxophone": instrument.AltoSaxophone(),
    "Bagpipes": instrument.Bagpipes(),
    "Banjo": instrument.Banjo(),
    "Baritone": instrument.Baritone(),
    "BaritoneSaxophone": instrument.BaritoneSaxophone(),
    "Bass": instrument.Bass(),
    "BassClarinet": instrument.BassClarinet(),
    "BassDrum": instrument.BassDrum(),
    "BassTrombone": instrument.BassTrombone(),
    "Bassoon": instrument.Bassoon(),
    "BongoDrums": instrument.BongoDrums(),
    "BrassInstrument": instrument.BrassInstrument(),
    "Castanets": instrument.Castanets(),
    "Celesta": instrument.Celesta(),
    "Choir": instrument.Choir(),
    "ChurchBells": instrument.ChurchBells(),
    "Clarinet": instrument.Clarinet(),
    "Clavichord": instrument.Clavichord(),
    "Conductor": instrument.Conductor(),
    "CongaDrum": instrument.CongaDrum(),
    "Contrabass": instrument.Contrabass(),
    "Contrabassoon": instrument.Contrabassoon(),
    "Cowbell": instrument.Cowbell(),
    "CrashCymbals": instrument.CrashCymbals(),
    "Cymbals": instrument.Cymbals(),
    "Dulcimer": instrument.Dulcimer(),
    "ElectricBass": instrument.ElectricBass(),
    "ElectricGuitar": instrument.ElectricGuitar(),
    "ElectricOrgan": instrument.ElectricOrgan(),
    "ElectricPiano": instrument.ElectricPiano(),
    "EnglishHorn": instrument.EnglishHorn(),
    "FingerCymbals": instrument.FingerCymbals(),
    "Flute": instrument.Flute(),
    "FretlessBass": instrument.FretlessBass(),
    "Glockenspiel": instrument.Glockenspiel(),
    "Gong": instrument.Gong(),
    "Guitar": instrument.Guitar(),
    "Handbells": instrument.Handbells(),
    "Harmonica": instrument.Harmonica(),
    "Harp": instrument.Harp(),
    "Harpsichord": instrument.Harpsichord(),
    "HiHatCymbal": instrument.HiHatCymbal(),
    "Horn": instrument.Horn(),
    "Kalimba": instrument.Kalimba(),
    "KeyboardInstrument": instrument.KeyboardInstrument(),
    "Koto": instrument.Koto(),
    "Lute": instrument.Lute(),
    "Mandolin": instrument.Mandolin(),
    "Maracas": instrument.Maracas(),
    "Marimba": instrument.Marimba(),
    "MezzoSoprano": instrument.MezzoSoprano(),
    "Oboe": instrument.Oboe(),
    "Ocarina": instrument.Ocarina(),
    "Organ": instrument.Organ(),
    "PanFlute": instrument.PanFlute(),
    "Percussion": instrument.Percussion(),
    "Piano": instrument.Piano(),
    "Piccolo": instrument.Piccolo(),
    "PipeOrgan": instrument.PipeOrgan(),
    "PitchedPercussion": instrument.PitchedPercussion(),
    "Ratchet": instrument.Ratchet(),
    "Recorder": instrument.Recorder(),
    "ReedOrgan": instrument.ReedOrgan(),
    "RideCymbals": instrument.RideCymbals(),
    "Sampler": instrument.Sampler(),
    "SandpaperBlocks": instrument.SandpaperBlocks(),
    "Saxophone": instrument.Saxophone(),
    "Shakuhachi": instrument.Shakuhachi(),
    "Shamisen": instrument.Shamisen(),
    "Shehnai": instrument.Shehnai(),
    "Siren": instrument.Siren(),
    "Sitar": instrument.Sitar(),
    "SizzleCymbal": instrument.SizzleCymbal(),
    "SleighBells": instrument.SleighBells(),
    "SnareDrum": instrument.SnareDrum(),
    "Soprano": instrument.Soprano(),
    "SopranoSaxophone": instrument.SopranoSaxophone(),
    "SplashCymbals": instrument.SplashCymbals(),
    "SteelDrum": instrument.SteelDrum(),
    "StringInstrument": instrument.StringInstrument(),
    "SuspendedCymbal": instrument.SuspendedCymbal(),
    "Taiko": instrument.Taiko(),
    "TamTam": instrument.TamTam(),
    "Tambourine": instrument.Tambourine(),
    "TempleBlock": instrument.TempleBlock(),
    "Tenor": instrument.Tenor(),
    "TenorDrum": instrument.TenorDrum(),
    "TenorSaxophone": instrument.TenorSaxophone(),
    "Timbales": instrument.Timbales(),
    "Timpani": instrument.Timpani(),
    "TomTom": instrument.TomTom(),
    "Triangle": instrument.Triangle(),
    "Trombone": instrument.Trombone(),
    "Trumpet": instrument.Trumpet(),
    "Tuba": instrument.Tuba(),
    "TubularBells": instrument.TubularBells(),
    "Ukulele": instrument.Ukulele(),
    "UnpitchedPercussion": instrument.UnpitchedPercussion(),
    "Vibraphone": instrument.Vibraphone(),
    "Vibraslap": instrument.Vibraslap(),
    "Viola": instrument.Viola(),
    "Violin": instrument.Violin(),
    "Violoncello": instrument.Violoncello(),
    "Vocalist": instrument.Vocalist(),
    "Whip": instrument.Whip(),
    "Whistle": instrument.Whistle(),
    "WindMachine": instrument.WindMachine(),
    "Woodblock": instrument.Woodblock(),
    "WoodwindInstrument": instrument.WoodwindInstrument(),
    "Xylophone": instrument.Xylophone()
}

def on_process_button_clicked():
  dialog = QDialog()
  dialog.setStyleSheet(PHRYGIAN_GUI)
  layout = QFormLayout()
  layout.setObjectName('QFormLayout')
  dialog.setWindowTitle(PROCESS_STRING)

  def set_midi_folder():
    text_browser_midi_folder.setText(str(QFileDialog.getExistingDirectory(None, "Select Directory")))

  def set_output_file():
    text_browser_output_file.setText(str(QFileDialog.getSaveFileName(None, 'Save File', '', '*.mid;;*.MID')))

  label_midi_folder = QLabel('Select a midi folder')
  label_output_midi = QLabel('File to save the generated melodies')
  label_midi_folder.setObjectName('QLabelRow')
  label_output_midi.setObjectName('QLabelRow')

  browser_button_midi = QPushButton('Browser...')
  browser_button_midi.setStyleSheet(PHRYGIAN_GUI)
  browser_button_output = QPushButton('Browser...')
  browser_button_output.setStyleSheet(PHRYGIAN_GUI)

  text_browser_midi_folder = QTextBrowser()
  text_browser_midi_folder.setObjectName('QTextBrowser')
  text_browser_midi_folder.setAcceptRichText(True)
  text_browser_midi_folder.setOpenExternalLinks(True)
  browser_button_midi.pressed.connect(set_midi_folder)
  layout.addWidget(text_browser_midi_folder)
  layout.addRow(label_midi_folder, text_browser_midi_folder)
  layout.addWidget(browser_button_midi)

  text_browser_output_file = QTextBrowser()
  text_browser_output_file.setObjectName('QTextBrowser')
  text_browser_output_file.setAcceptRichText(True)
  text_browser_output_file.setOpenExternalLinks(True)
  browser_button_output.pressed.connect(set_output_file)
  layout.addWidget(text_browser_output_file)
  layout.addRow(label_output_midi, text_browser_output_file)
  layout.addWidget(browser_button_output)

  dialog.setLayout(layout)
  dialog.exec()

def on_generate_button_clicked():
  dialog = QDialog()
  layout = QFormLayout()
  layout.setObjectName('QFormLayout')
  dialog.setWindowTitle(GENERATE_STRING)

  def set_processed_midi():
    text_browser_processed_midi.setText(str(QFileDialog.getOpenFileName (None, 'Select processed midi file')))

  def set_weights_file():
    text_browser_weights.setText(str(QFileDialog.getOpenFileName(None, "Select neural networks weights")))

  label_processed_midi = QLabel('Select a processed midi file')
  label_weights = QLabel('Select a folder to save the generated melodies')
  label_pitch = QLabel('Select the pitch ')
  label_scale = QLabel('Select the scale')
  label_notes = QLabel('Select the number of notes')
  label_instruments = QLabel('Select the instrument')
  label_output_midi = QLabel('Write output midi file')

  browser_button_midi = QPushButton('Browser...')
  browser_button_nw = QPushButton('Browser...')

  combo_box_pitch = QComboBox()
  combo_box_pitch.addItems([chr(i) for i in range(ord('A'), ord('G') + 1)])
  layout.addWidget(combo_box_pitch)
  layout.addRow(label_pitch, combo_box_pitch)

  combo_box_instruments = QComboBox()
  combo_box_instruments.addItems(INSTRUMENTS.keys())
  layout.addWidget(combo_box_instruments)
  layout.addRow(label_instruments, combo_box_instruments)

  spin_box_scale = QSpinBox()
  spin_box_scale.setRange(1, 8)
  layout.addWidget(spin_box_scale)
  layout.addRow(label_scale, spin_box_scale)

  spin_box_notes = QSpinBox()
  spin_box_notes.setRange(2, 9999)
  layout.addWidget(spin_box_notes)
  layout.addRow(label_notes, spin_box_notes)

  text_browser_processed_midi = QTextBrowser()
  text_browser_processed_midi.setAcceptRichText(True)
  text_browser_processed_midi.setOpenExternalLinks(True)
  browser_button_midi.pressed.connect(set_processed_midi)
  layout.addWidget(text_browser_processed_midi)
  layout.addRow(label_processed_midi, text_browser_processed_midi)
  layout.addWidget(browser_button_midi)

  text_browser_weights = QTextBrowser()
  text_browser_weights.setAcceptRichText(True)
  text_browser_weights.setOpenExternalLinks(True)
  browser_button_nw.pressed.connect(set_weights_file)
  layout.addWidget(text_browser_weights)
  layout.addRow(label_weights, text_browser_weights)
  layout.addWidget(browser_button_nw)

  output_midi_file  = QLineEdit()
  output_midi_file.move(80, 20)
  output_midi_file.resize(200, 32)
  layout.addWidget(output_midi_file)
  layout.addRow(label_output_midi, output_midi_file)
  
  dialog.setLayout(layout)
  dialog.exec()

def on_train_button_clicked():
  dialog = QDialog()
  layout = QFormLayout()
  layout.setObjectName('QFormLayout')
  dialog.setWindowTitle(TRAIN_STRING)

  def set_processed_midi():
    text_browser_processed_midi.setText(str(QFileDialog.getOpenFileName (None, 'Select processed midi file')))

  def set_weights_folder():
    text_browser_weights_folder.setText(str(QFileDialog.getExistingDirectory(None, "Select Directory")))

  label_processed_midi = QLabel('Select processed midi')
  label_wights_folder = QLabel('Select neural network weights folder')

  browser_button_midi = QPushButton('Browser...')
  browser_button_wights = QPushButton('Browser...')

  text_browser_processed_midi = QTextBrowser()
  text_browser_processed_midi.setAcceptRichText(True)
  text_browser_processed_midi.setOpenExternalLinks(True)
  browser_button_midi.pressed.connect(set_processed_midi)
  layout.addWidget(text_browser_processed_midi)
  layout.addRow(label_processed_midi, text_browser_processed_midi)
  layout.addWidget(browser_button_midi)

  text_browser_weights_folder = QTextBrowser()
  text_browser_weights_folder.setAcceptRichText(True)
  text_browser_weights_folder.setOpenExternalLinks(True)
  browser_button_wights.pressed.connect(set_weights_folder)
  layout.addWidget(text_browser_weights_folder)
  layout.addRow(label_wights_folder, text_browser_weights_folder)
  layout.addWidget(browser_button_wights)

  dialog.setLayout(layout)
  dialog.exec()

app = QApplication([])

window = QWidget()
window.setWindowTitle("Phrygian")
window.setStyleSheet(PHRYGIAN_GUI)
layout = QVBoxLayout()
layout.setSizeConstraint(QLayout.SetFixedSize)

label_welcome = QLabel('WELCOME TO PHRYGIAN')
layout.addWidget(label_welcome)
label_welcome.setObjectName('label_welcome')

process_button = QPushButton(PROCESS_STRING)
train_button = QPushButton(TRAIN_STRING)
generate_button = QPushButton(GENERATE_STRING)

layout.addWidget(process_button)
layout.addWidget(train_button)
layout.addWidget(generate_button)

process_button.clicked.connect(on_process_button_clicked)
train_button.clicked.connect(on_train_button_clicked)
generate_button.clicked.connect(on_generate_button_clicked)

window.setLayout(layout)
window.show()
app.exec()
