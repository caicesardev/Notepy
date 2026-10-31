DEFAULT_ZOOM_PERCENT = 100
MIN_ZOOM_PERCENT = 10
MAX_ZOOM_PERCENT = 500
ZOOM_STEP_PERCENT = 10
MIN_POINT_SIZE = 1.0


def clamp_zoom(percent: int) -> int:
    return max(MIN_ZOOM_PERCENT, min(MAX_ZOOM_PERCENT, percent))


def zoomed_point_size(base_point_size: float, zoom_percent: int) -> float:
    return max(MIN_POINT_SIZE, base_point_size * zoom_percent / DEFAULT_ZOOM_PERCENT)
