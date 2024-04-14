import dash
from dash import Input, Output, html
import dash_mantine_components as dmc
import pyaudio
import wave
import threading

# Configurações de áudio
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
WAVE_OUTPUT_FILENAME = "output.wav"

# Inicialização do PyAudio
audio = pyaudio.PyAudio()

# Variáveis de controle
recording = False

# Função para gravar áudio
def record_audio():
    global recording
    frames = []
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    # print("Gravação iniciada...")
    while recording:
        data = stream.read(CHUNK)
        frames.append(data)
    # print("Gravação finalizada.")
    stream.stop_stream()
    stream.close()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# Criação do aplicativo Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Iniciar Gravação', id='start-button', n_clicks=0),
    html.Button('Finalizar Gravação', id='stop-button', n_clicks=0),
    html.Div(id='output-message' , style={"width":"200px"})
])

# Callbacks para os botões
@app.callback(
    Output('output-message', 'children'),
    [Input('start-button', 'n_clicks'),
     Input('stop-button', 'n_clicks')]
)
def update_output(start_clicks, stop_clicks):
    global recording
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'start-button' in changed_id:
        if start_clicks > 0:
            threading.Thread(target=record_audio).start()
            recording = True
            return html.Div([
                dmc.Alert("Gravação iniciada...",ta="center"),
                dmc.Center(dmc.Loader(size="md", variant="bars",))

            ])
    elif 'stop-button' in changed_id:
        if stop_clicks > 0:
            recording = False
            return dmc.Alert("Gravação finalizada.",color="green",ta="center", duration=2000)

if __name__ == '__main__':
    app.run_server(debug=True)