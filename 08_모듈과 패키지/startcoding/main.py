# 1. import 패키지.모듈
import unit.character
unit.character.test()

# 2. from 패키지 import 모듈 -> 1번보다 더 많이 사용
from unit import item
item.test()

# 3. from 패키지 import *  -> __init__.py에 from . import character, item, monster 생성해야함
# from unit import *
# character.test()
# item.test()
# monster.test()

# 4. import 패키지 -> __init__.py에 from . import character, item, monster 생성해야함
import unit
unit.character.test()
unit.item.test()
unit.monster.test()