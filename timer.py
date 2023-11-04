# pygameをインポートする
import pygame

# pygameを初期化する
pygame.init()

# 画面のサイズを設定する
screen = pygame.display.set_mode((800, 600))

# 画面のタイトルを設定する
pygame.display.set_caption('ストップウォッチ')

# 時間を管理するためのクロックを作成する
clock = pygame.time.Clock()

# ストップウォッチの状態を表す変数を定義する

# ストップウォッチが動いているかどうか
running = False
# ストップウォッチを開始した時刻
start_time = 0
# ストップウォッチの経過時間
elapsed_time = 0
# 前回の秒数
last_time = 0

# フォントを作成する
font = pygame.font.SysFont('Arial', 64)

# ボタンの位置とサイズを定義する
start_button = pygame.Rect(100, 400, 200, 100)
stop_button = pygame.Rect(300, 400, 200, 100)
reset_button = pygame.Rect(500, 400, 200, 100)

# ボタンの色を定義する
button_color = (200, 200, 200)
button_hover_color = (150, 150, 150)

# ボタンのテキストを作成する
start_text = font.render('start', True, (0, 0, 0))
stop_text = font.render('stop', True, (0, 0, 0))
reset_text = font.render('reset', True, (0, 0, 0))

# ボタンのテキストの位置を計算する
start_text_rect = start_text.get_rect()
start_text_rect.center = start_button.center
stop_text_rect = stop_text.get_rect()
stop_text_rect.center = stop_button.center
reset_text_rect = reset_text.get_rect()
reset_text_rect.center = reset_button.center

# 音をロードする
sound = pygame.mixer.Sound("./Hi-Hat-Closed-Hit.mp3")

# メインループ
while True:
    # イベントを処理する
    for event in pygame.event.get():
        # 終了イベントがあればプログラムを終了する
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # マウスのクリックイベントがあれば
        if event.type == pygame.MOUSEBUTTONDOWN:
            # マウスの位置を取得する
            mouse_pos = pygame.mouse.get_pos()
            # スタートボタンがクリックされたら
            if start_button.collidepoint(mouse_pos):
                # ストップウォッチを開始する
                running = True
                start_time = pygame.time.get_ticks()
            # ストップボタンがクリックされたら
            if stop_button.collidepoint(mouse_pos):
                # ストップウォッチを停止する
                running = False
            # リセットボタンがクリックされたら
            if reset_button.collidepoint(mouse_pos):
                # ストップウォッチをリセットする
                running = False
                elapsed_time = 0
                last_time = 0

    # 画面を白色で塗りつぶす
    screen.fill((255, 255, 255))

    # ストップウォッチが動いているなら
    if running:
        # 経過時間を更新する
        elapsed_time = pygame.time.get_ticks() - start_time
        # 経過時間をミリ秒から秒に変換する
        seconds = elapsed_time // 1000
        # 秒数が変わったら
        if seconds != last_time:
            # 音を再生する
            sound.play()
            # 前回の秒数を更新する
            last_time = seconds

    # 経過時間を文字列に変換する
    time_string = f"{elapsed_time // 60000:02d}: \
{elapsed_time % 60000 // 1000:02d}.{elapsed_time % 1000 // 10:02d}"

    # 経過時間を画面に描画する
    time_text = font.render(time_string, True, (0, 0, 0))
    time_text_rect = time_text.get_rect()
    time_text_rect.center = (400, 200)
    screen.blit(time_text, time_text_rect)

    # マウスの位置を取得する
    mouse_pos = pygame.mouse.get_pos()

    # スタートボタンを画面に描画する
    if start_button.collidepoint(mouse_pos):
        # マウスがボタンの上にあれば色を変える
        pygame.draw.rect(screen, button_hover_color, start_button)
    else:
        # マウスがボタンの上になければ色をそのままにする
        pygame.draw.rect(screen, button_color, start_button)
    # スタートボタンのテキストを画面に描画する
    screen.blit(start_text, start_text_rect)

    # ストップボタンを画面に描画する
    if stop_button.collidepoint(mouse_pos):
        # マウスがボタンの上にあれば色を変える
        pygame.draw.rect(screen, button_hover_color, stop_button)
    else:
        # マウスがボタンの上になければ色をそのままにする
        pygame.draw.rect(screen, button_color, stop_button)
    # ストップボタンのテキストを画面に描画する
    screen.blit(stop_text, stop_text_rect)

    # リセットボタンを画面に描画する
    if reset_button.collidepoint(mouse_pos):
        # マウスがボタンの上にあれば色を変える
        pygame.draw.rect(screen, button_hover_color, reset_button)
    else:
        # マウスがボタンの上になければ色をそのままにする
        pygame.draw.rect(screen, button_color, reset_button)
    # リセットボタンのテキストを画面に描画する
    screen.blit(reset_text, reset_text_rect)

    # 画面を更新する
    pygame.display.flip()

    # フレームレートを60に設定する
    clock.tick(60)
