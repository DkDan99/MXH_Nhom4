# Dự đoán Xếp loại Tốt nghiệp Sinh viên UIT dựa trên Mạng Xã hội

## Mô tả

Đồ án này ứng dụng phân tích mạng xã hội (SNA) và học máy để dự đoán xếp loại tốt nghiệp của sinh viên trường Đại học Công nghệ Thông tin (UIT). 

## Tập dữ liệu

* **Nguồn:**  Dữ liệu được cung cấp bởi trường Đại học Công nghệ Thông tin.
* **Mô tả:**  Tập dữ liệu chứa thông tin của 1831 sinh viên với 46 thuộc tính, bao gồm thông tin cá nhân, kết quả học tập, điểm rèn luyện và xếp loại tốt nghiệp.

## Các bước thực hiện

1. **Khám phá dữ liệu:** Phân tích, thống kê mô tả và trực quan hóa dữ liệu để hiểu rõ hơn về đặc điểm của tập dữ liệu.
2. **Tiền xử lý dữ liệu:** Làm sạch, chuyển đổi và rút gọn dữ liệu để chuẩn bị cho việc xây dựng mạng xã hội.
3. **Xây dựng mạng xã hội:** 
    * Xác định nút và cạnh dựa trên các thuộc tính đã chọn (điểm trung bình học kỳ, số tín chỉ tích lũy, phân cụm).
    * Tính toán trọng số cạnh dựa trên mức độ tương đồng giữa các sinh viên.
    * Gán nhãn cho các nút bằng xếp loại tốt nghiệp.
4. **Phân tích mạng xã hội:** Phân tích cấu trúc mạng và trực quan hóa mạng lưới.
5. **Xây dựng mô hình dự đoán:** 
    * Lựa chọn các mô hình học máy (Logistic Regression, SVM, Decision Tree, KNN).
    * Huấn luyện và đánh giá mô hình trên tập dữ liệu đã xử lý.
6. **Đánh giá kết quả:** So sánh hiệu quả của các mô hình và đánh giá hiệu quả của phương pháp.

## Code

* `data_processing.py`:  Code tiền xử lý dữ liệu, bao gồm làm sạch, chuyển đổi, rút gọn dữ liệu và lưu vào file "data_sampled.csv".
* `data_visualization.py`:  Code trực quan hóa dữ liệu, bao gồm các biểu đồ histogram, boxplot, scatter plot, heatmap.
* `network_construction.py`:  Code xây dựng mạng xã hội, bao gồm tạo nút, cạnh, trọng số và gán nhãn.
* `network_analysis.py`:  Code phân tích mạng xã hội, bao gồm tính toán các chỉ số mạng và trực quan hóa mạng lưới.
* `prediction_models.py`:  Code xây dựng và đánh giá các mô hình học máy.

## Thư viện

* pandas
* scikit-learn
* matplotlib
* seaborn
* networkx

## Cách chạy code

1. Cài đặt các thư viện cần thiết.
2. Chạy file `data_processing.py` để tiền xử lý dữ liệu.
3. Chạy file `data_visualization.py` để trực quan hóa dữ liệu.
4. Chạy file `network_construction.py` để xây dựng mạng xã hội.
5. Chạy file `network_analysis.py` để phân tích mạng xã hội.
6. Chạy file `prediction_models.py` để xây dựng và đánh giá mô hình dự đoán.

## Kết quả

* Mô hình SVM cho kết quả tốt nhất với F1-score (macro) đạt 0.78 và F1-score (weighted) đạt 0.82.
* Việc kết hợp phân tích mạng xã hội giúp cải thiện hiệu quả dự đoán so với việc chỉ sử dụng các đặc trưng truyền thống.

## Hướng phát triển

* Mở rộng nguồn dữ liệu.
* Mở rộng quy mô mạng.
* Nghiên cứu sâu hơn về cấu trúc mạng và ứng dụng các thuật toán học máy nâng cao.
* Xây dựng ứng dụng web/mobile.

## Nhóm tác giả

* 21521916 - Đỗ Khánh Đan
* 21521201 - Nguyễn Đỗ Đức Nguyên
* 21522326 - Trần Thanh Mẫn
* 21521183 - Nguyễn Thành Nghĩa
