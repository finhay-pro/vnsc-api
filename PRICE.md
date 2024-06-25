# Getting started
Install python requirements:
``` pip install -r requirements.txt ```

Run sample code:
```
python sample.py
```

# Stock Price Message

Here is a sample data of Stock Price Message:
```
{
  "price": 14200,           # giá khớp gần nhất
  "bid1": 14200,            # giá cao nhất bên mua
  "offer1": 14250,          # giá thấp nhất bên bán
  "bid2": 14150,            # giá cao thứ 2 bên mua
  "offer2": 14300,          # giá cao thứ 2 bên bán
  "bid3": 14100,            # giá cao thứ 3 bên mua
  "offer3": 14350,          # giá cao thứ 3 bên bán
  "bid1Vol": "69700",       # khối lượng dư mua ứng với giá cao nhất bên mua
  "offer1Vol": "54300",     # khối lượng dư bán ứng với giá thấp nhất bên bán
  "bid2Vol": "154000",
  "offer2Vol": "146000",
  "bid3Vol": "122300",
  "offer3Vol": "78500",
  "changePercent": 0.3533569, # Thay đổi giá gần nhất, đơn vị: %
  "symbol": "MSB",
  "change": 50,               # Thay đổi giá gần nhất, đơn vị: đồng
  "vol": "400",               # Thay đổi khối lượng (khối lượng khớp) gần nhất, đơn vị: 1 cổ
  "foreignBought": "16774407", # Số lượng cổ phiếu Nhà đầu tư nước ngoài đặt mua
  "foreignSold": "16700600",   # Số lượng cổ phiếu Nhà đầu tư nước ngoài đặt bán
  "foreignRemain": "14102032", # Số lượng cổ phiếu Nhà đầu tư nước ngoài còn lại
  "totalVol": "1392100",        # Tổng số lượng cổ đã khớp, đơn vị: 1 cổ
  "totalVal": "19756590000",    # Tổng giá trị đã khớp, đơn vị: đồng
  "high": 14250,                # Giá khớp cao nhất phiên
  "medium": 14191,              # Giá khớp trung bình
  "low": 14100,                 # Giá khớp thấp nhất phiên
  "ceiling": 15100,             # Giá trần
  "reference": 14150,           # Giá tham chiếu
  "floor": 13200,               # Giá sàn
}
```

Note:
1. `Price/Change` is usually in `1 VND` unit.
2. `Val` is usually value, also in `1 VND` unit.
3. `Vol` is usually volume (stock quantity), in `1 stock` unit.