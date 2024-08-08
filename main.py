import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

video = cv2.VideoCapture(0)

video.set(3, 1280)
video.set(4, 720)

kb = Controller()

detector = HandDetector(detectionCon=0.8)
estadoAtual = [0, 0, 0, 0, 0]

while True:
    _, img = video.read()
    hands, img = detector.findHands(img)

    if hands:
        estado = detector.fingersUp(hands[0])

        # Jogo do T-Rex -------------------------------------------
        if estado == [1, 1, 1, 1, 1]:  # Mão aberta
            if estadoAtual != estado:
                print('Pular')
                kb.press(Key.space)
                kb.release(Key.space)
        # -------------------------------------------------------------|

        # Passador de Slides -------------------------------------------
        #if estado == [0, 0, 0, 0, 1]:  # Apenas o mindinho levantado
        #    if estadoAtual != estado:
        #        print('Direita')
        #        kb.press(Key.right)
        #        kb.release(Key.right)
        #
        #elif estado == [1, 0, 0, 0, 0]:  # Apenas o dedão levantado
        #    if estadoAtual != estado:
        #        print('Esquerda')
        #        kb.press(Key.left)
        #        kb.release(Key.left)
        # -------------------------------------------------------------|

        # Pause/Reproduzir Música -------------------------------------|
        #if estado == [1, 1, 1, 1, 1]:  # Mão Aberta
        #    if estadoAtual != estado:
        #        print('Pausar/Reproduzir')
        #        kb.press(Key.media_play_pause)  # Comando para pausar ou reproduzir
        #        kb.release(Key.media_play_pause)
        #
        # Próxima Música
        #elif estado == [1, 1, 0, 0, 0]:  # Apenas o dedo polegar e o indicador levantados
        #    if estadoAtual != estado:
        #        print('Próxima Música')
        #        kb.press(Key.media_next)
        #        kb.release(Key.media_next)
        # Música Anterior
        #elif estado == [0, 1, 1, 0, 0]:  # Apenas o dedo indicador e médio levantados
        #    if estadoAtual != estado:
        #        print('Música Anterior')
        #        kb.press(Key.media_previous)
        #        kb.release(Key.media_previous)
        # -------------------------------------------------------------|


        estadoAtual = estado

    cv2.imshow('Video ', cv2.resize(img, (640, 420)))
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()