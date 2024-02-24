import pyautogui as pag

# Setting up failsafe
pag.FAILSAFE = True

def p(size, duration):
    seg = size * (1 / 8)

    pag.dragRel(0, -size, duration=duration, button='left')
    pag.dragRel(seg * 7, 0, duration=duration, button='left')
    pag.dragRel(seg, seg, duration=duration, button='left')
    pag.dragRel(0, seg * 2, duration=duration, button='left')
    pag.dragRel(-seg, seg, duration=duration, button='left')
    pag.dragRel(-seg * 6, 0, duration=duration, button='left')

    pag.moveRel(seg, 0, duration=duration)