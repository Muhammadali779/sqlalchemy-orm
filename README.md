Yangi model qoshing xuddi Score model kabi

# **Certificate modeli** quyidagicha bo‘ladi:

| Field              | Type          | Izoh                                |
| ------------------ | ------------- | ----------------------------------- |
| `student_id`       | FK → Student  | Sertifikat kimga berilgan           |
| `title`            | String        | Sertifikat nomi                     |
| `content`          | Text/String   | Sertifikat mazmuni yoki description |
| `issued_at`        | DateTime      | Berilgan vaqt (default = now)       |
| `certificate_code` | String unique | Unikal sertifikat kodi              |
| `is_verified`      | Boolean       | Tekshirilgan/yo‘q                   |

---

# 🟩 **Student modeliga qo‘shish**

```python
# Student modeli ichida
certificates = relationship('Certificate', back_populates='student')
```

---

# 🟧 **Uyga vazifa — Certificate bilan practice**

### **1. Insert**

1. Student 1 uchun yangi certificate qo‘sh: `title="Python Basics"`, `content="Completed course"`, `certificate_code` random orqali yarating
2. Student 2 uchun 2 ta certificate qo‘sh

### **2. Query**

3. Barcha certificate larni oling
4. `is_verified=False` bo‘lgan certificate lar
5. Berilgan `student_id` uchun barcha certificate lar
6. certificate_code bo‘yicha certificate qidirish
7. issued_at bo‘yicha 5 ta oxirgi certificate

### **3. Update**

8. certificate_code bo‘yicha is_verified=True qil

### **5. Aggregation**

9. Studentlar bo‘yicha certificate soni
10. Eng ko‘p certificate olgan student
111. is_verified bo‘lgan certificate larni count qilish
