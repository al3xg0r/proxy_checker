# HTTPS Proxy Checker

A fast and simple HTTPS proxy checker using only ProxyScrape as a reliable source. It downloads 30,000+ fresh proxies, checks them via two public IP-detection services, and saves the working ones in ProxyCap-compatible format.

## 🔧 Features

- ✅ **Only ProxyScrape** as the source (stable, large pool)
- 🚀 **Multithreaded** (60 threads)
- ⏱ **20-second timeout** per proxy
- 🧪 **Dual checking**: `icanhazip.com` and `api.ip.sb`
- 💾 **Saves live proxies** to `live_https_proxies_proxycap.txt` (`IP,Port,HTTPS`)
- 🧹 No logging of successful checks
- ⚠️ Only logs proxy source errors to `proxy_checker.log`
- 📊 Real-time **progress percentage** in console

## ▶️ Usage

### 1. Install dependencies

```bash
pip install requests
```

### 2. Run the checker

```bash
python proxy_checker.py
```

### 3. Output files

- ✅ `live_https_proxies_proxycap.txt` — working proxies
- ⚠️ `proxy_checker.log` — only critical loading errors (if any)

---

# Чекер HTTPS-прокси

Быстрый и простой чекер HTTPS-прокси, использующий только ProxyScrape как проверенный и стабильный источник. Загружает более 30 000 прокси, проверяет их через два IP-сервиса и сохраняет рабочие в формате ProxyCap.

## 🔧 Возможности

- ✅ Только **ProxyScrape** как источник (большая и стабильная база)
- 🚀 **Многопоточная** проверка (60 потоков)
- ⏱ **Таймаут 20 секунд** на прокси
- 🧪 **Двойная проверка** через `icanhazip.com` и `api.ip.sb`
- 💾 **Сохранение живых прокси** в `live_https_proxies_proxycap.txt` (`IP,Port,HTTPS`)
- 🧹 Не логирует успешные подключения
- ⚠️ Логирует **только ошибки загрузки** в `proxy_checker.log`
- 📊 **Процент выполнения** в режиме реального времени

## ▶️ Использование

### 1. Установить зависимости

```bash
pip install requests
```

### 2. Запустить чекер

```bash
python proxy_checker.py
```

### 3. Результирующие файлы

- ✅ `live_https_proxies_proxycap.txt` — живые прокси
- ⚠️ `proxy_checker.log` — только ошибки получения (если есть)

## 📄 Лицензия

MIT License
