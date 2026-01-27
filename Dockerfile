# Chọn hệ điều hành nền (Base Image) có sẵn Python
FROM python:3.13.5

# Thiết lập thư mục làm việc bên trong container
WORKDIR /usr/src/app

# Copy file requirements.txt từ máy thật vào container
COPY requirements.txt ./

# Cài đặt các thư viện
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code từ máy thật vào thư mục /usr/src/app trong container
COPY . .


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]