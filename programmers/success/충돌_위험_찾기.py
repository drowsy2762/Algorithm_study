# 2026-06-07


def solution(points, routes):
    point_map = {}
    for idx in range(len(points)):
        point_map[idx + 1] = points[idx]

    all_robot_paths = []

    for route in routes:
        robot_path = []
        start_point_id = route[0]
        curr_r = point_map[start_point_id][0]
        curr_c = point_map[start_point_id][1]
        robot_path.append((curr_r, curr_c))

        for i in range(1, len(route)):
            next_point_id = route[i]
            target_r = point_map[next_point_id][0]
            target_c = point_map[next_point_id][1]

            while curr_r != target_r:
                if curr_r < target_r:
                    curr_r += 1
                else:
                    curr_r -= 1
                robot_path.append((curr_r, curr_c))

            while curr_c != target_c:
                if curr_c < target_c:
                    curr_c += 1
                else:
                    curr_c -= 1
                robot_path.append((curr_r, curr_c))

        all_robot_paths.append(robot_path)

    max_time = 0
    for path in all_robot_paths:
        if len(path) > max_time:
            max_time = len(path)

    danger_count = 0

    for t in range(max_time):
        position_counts = {}

        for path in all_robot_paths:
            if t < len(path):
                current_position = path[t]
                if current_position in position_counts:
                    position_counts[current_position] += 1
                else:
                    position_counts[current_position] = 1

        for count in position_counts.values():
            if count >= 2:
                danger_count += 1

    return danger_count
