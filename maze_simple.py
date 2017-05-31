"""迷路探索シミュレータ

用意された迷路において、出発点sから探索を開始する。
探索する際に歩いた場所に歩数を記録していく。

Note:
迷路は2次元格子空間であり、次のように2重リストにより表現する。

    maze = ['#######',
            '#s    #',
            '# #####',
            '#   # #',
            '# ### #',
            '#     #',
            '#######']

    map = [['#', '#', '#', '#', '#', '#', '#'],
           ['#', 's', ' ', ' ', ' ', ' ', '#'],
           ['#', ' ', '#', '#', '#', '#', '#'],
           ['#', ' ', ' ', ' ', '#', ' ', '#'],
           ['#', ' ', '#', '#', '#', ' ', '#'],
           ['#', ' ', ' ', ' ', ' ', ' ', '#'],
           ['#', '#', '#', '#', '#', '#', '#']]

     - '#': 壁(移動できない)
     - 's': 出発点
     - ' ': 移動可能なマス

上記の maze と map は、共に同じ迷路を異なる方法で表現して使い分けている。
mazeはシステム側で用意した迷路そのものであり、変更しない（させない）。
mapは探索する際に利用し、まだ歩いていない場所 ' ' へ歩数を記録していく。


Example:
    case 1:
        % python3 maze_simple.py
    case 2:
        % python3
        > import maze_simple
        > maze_simple.test_play()
"""


def init_maze():
    """迷路と出発点を用意する。
    
    2次元格子空間の迷路を次のように表現する。
     - '#': 壁(移動できない)
     - 's': 出発点
     - ' ': 移動可能なマス
    
    冒頭で maze = ['str型オブジェクト', '同様',,,] として迷路を表現しているが、
    これは設定しやすくするために用意したデータである。実際に処理に使う際には、
    copy_maze_to_map()により「1文字ずつ分割した迷路」として表現している。
    
    Returns:
        map: 1文字ずつに分解された迷路を2重リストで表現。
        start_y, start_x: 迷路における出発点。
          *note: 出発点は「map[start_y][start_x]」。
    """
    maze = ['#######',
            '#s    #',
            '# #####',
            '#   # #',
            '# ### #',
            '#     #',
            '#######']
    map = copy_maze_to_map(maze)
    start_y, start_x = get_start(map)
    return map, start_y, start_x

def copy_maze_to_map(map):
    """1文字ずつ分割した迷路を用意。
    """
    result = []
    for line in map:
        new_line = []
        for char in line:
            new_line.append(char)
        result.append(new_line)
    return result

def print_map(map):
    """迷路を見やすい形に出力。
    """
    for line in map:
        for char in line:
            if type(char) == str:
                print(char, end='')
            else:
                first_digit = int(char) % 10
                print('{0}'.format(first_digit), end='')
        print()

def get_start(map):
    """用意された迷路における出発点('s'の位置)を返す。
    Note: 見つからない場合には False, False を返す。
    """
    y = 0
    for y_line in map:
        x = 0
        for x_place in y_line:
            if x_place == 's':
                return y, x
            else:
                x += 1
        y += 1
    
    return False, False

def is_upward(map, y, x):
    """map[y][x]を基点として、上方向(y-1)に移動可能かを判定する。
    移動可能なら True、できないなら Falseを返す。
    """
    target_y = y - 1
    target_x = x
    if target_y >= 0:
        return is_space(map, target_y, target_x)
    else:
        return False

def is_rightward(map, y, x):
    """map[y][x]を基点として、右方向(x+1)に移動可能かを判定する。
    移動可能なら True、できないなら Falseを返す。
    """
    target_y = y
    target_x = x + 1
    if target_x < len(map):
        return is_space(map, target_y, target_x)
    else:
        return False

def is_downward(map, y, x):
    """map[y][x]を基点として、下方向(y+1)に移動可能かを判定する。
    移動可能なら True、できないなら Falseを返す。
    """
    target_y = y + 1
    target_x = x
    if target_y < len(map):
        return is_space(map, target_y, target_x)
    else:
        return False

def is_leftword(map, y, x):
    """map[y][x]を基点として、左方向(x-1)に移動可能かを判定する。
    移動可能なら True、できないなら Falseを返す。
    """
    target_y = y
    target_x = x - 1
    if target_x >= 0:
        return is_space(map, target_y, target_x)
    else:
        return False

def is_space(map, y, x):
    """map[y][x]が移動可能かつ、まだ移動していない状態かどうかを判定する。
    移動可能なら True、できないなら Falseを返す。
    """
    if map[y][x] == ' ':
        return True
    else:
        return False

def walk_map_with_step_num(map, y, x, step_num):
    """map[y][x]からstep_numを歩数として歩数カウントする。
    """
    print('map[{0}][{1}]を基点とする探索を開始します。'.format(y, x))
    
    if is_upward(map, y, x) == True:
        step_num += 1
        map[y-1][x] = step_num
        print('上方向に移動します。(歩数={0})'.format(step_num))
        print_map(map)
        walk_map_with_step_num(map, y-1, x, step_num)
    
    if is_rightward(map, y, x) == True:
        step_num += 1
        map[y][x+1] = step_num
        print('右方向に移動します。(歩数={0})'.format(step_num))
        print_map(map)
        walk_map_with_step_num(map, y, x+1, step_num)
    
    if is_downward(map, y, x) == True:
        step_num += 1
        map[y+1][x] = step_num
        print('下方向に移動します。(歩数={0})'.format(step_num))
        print_map(map)
        walk_map_with_step_num(map, y+1, x, step_num)
    
    if is_leftword(map, y, x) == True:
        step_num += 1
        map[y][x-1] = step_num
        print('左方向に移動します。(歩数={0})'.format(step_num))
        print_map(map)
        walk_map_with_step_num(map, y, x-1, step_num)
    
    print('map[{0}][{1}]を基点とする探索を終了します。'.format(y, x))

def test_play():
    map, start_y, start_x = init_maze()
    print('探索を開始します')
    print_map(map)
    walk_map_with_step_num(map, start_y, start_x, 0)
    print('探索を終了しました')

if __name__ == '__main__':
    test_play()
