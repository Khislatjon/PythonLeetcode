from typing import List
def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []
    for ast in asteroids:
        while stack and ast < 0 < stack[-1]:
            diff = ast + stack[-1]
            if diff < 0:
                stack.pop()
                continue
            elif diff == 0:
                stack.pop()
            break
        else:
            stack.append(ast)
    return stack