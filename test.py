import pyproj

def proj_latlon(lat, lon):
    # 创建坐标转换器
    transformer = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:32632", always_xy=True)
    # 将经纬度转换为 UTM 坐标
    x, y = transformer.transform(lon, lat)
    return x, y

# 输入坐标
lat = 49.015003823272
lon = 8.4342971002335

# 转换为 UTM 坐标
x, y = proj_latlon(lat, lon)
print(f"UTM 坐标 (x, y): {x}, {y}")
