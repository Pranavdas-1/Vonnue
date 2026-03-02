"""
config.py — Criteria configuration for Casual Buyer mode (single mode).

No other modes exist. TOPSIS engine is not modified here.
"""

from typing import Any


# ──────────────────────────────────────────────────────
#  Dropdown maps
# ──────────────────────────────────────────────────────

APP_SUPPORT_MAP = {
    "No": 0,
    "Yes": 5,
}

BRAND_RELIABILITY_MAP = {
    "Low": 1,
    "Medium": 3,
    "High": 5,
}

STAND_ORIENTATION_MAP = {
    "Horizontal Only": 1,
    "Vertical Only": 1,
    "Both (Flexible)": 5,
}


# ──────────────────────────────────────────────────────
#  Criteria configuration
# ──────────────────────────────────────────────────────

CRITERIA_KEYS = [
    "price", "physical_weight",
    "clarity", "bass", "wattage", "battery",
    "charging_wattage", "build", "ip",
    "bluetooth", "multi_pair", "mic",
    "drivers", "app_support", "warranty",
    "brand_reliability", "stand_orientation",
    "battery_size",
]

CRITERIA_TYPES = {
    "price": "cost", "physical_weight": "cost",
    "clarity": "benefit", "bass": "benefit", "wattage": "benefit",
    "battery": "benefit", "charging_wattage": "benefit",
    "build": "benefit", "ip": "benefit", "bluetooth": "benefit",
    "multi_pair": "benefit", "mic": "benefit",
    "drivers": "benefit", "app_support": "benefit", "warranty": "benefit",
    "brand_reliability": "benefit", "stand_orientation": "benefit",
    "battery_size": "benefit",
}

CRITERIA_LABELS = {
    "price": "Price (₹)", "physical_weight": "Weight (kg)",
    "clarity": "Sound Clarity", "bass": "Bass Strength",
    "wattage": "Loudness (Wattage)", "battery": "Battery Life (Hours)",
    "charging_wattage": "Charging Wattage", "build": "Build Quality",
    "ip": "IP Rating", "bluetooth": "Bluetooth Version",
    "multi_pair": "Multi-Pairing Support", "mic": "Microphone Support",
    "drivers": "Number of Drivers", "app_support": "App Support",
    "warranty": "Warranty (Years)",
    "brand_reliability": "Brand Reliability",
    "stand_orientation": "Stand Orientation",
    "battery_size": "Battery Size (mAh)",
}

DIRECTION_OVERRIDABLE = ["price", "physical_weight"]

ICONS = {
    "price": "💰", "physical_weight": "⚖️",
    "clarity": "🔉", "bass": "🎵", "wattage": "📢",
    "battery": "🔋", "charging_wattage": "⚡",
    "build": "🏗️", "ip": "💧", "bluetooth": "📶",
    "multi_pair": "🔗", "mic": "🎤",
    "drivers": "🔈", "app_support": "📱", "warranty": "🛡️",
    "brand_reliability": "⭐", "stand_orientation": "🔄",
    "battery_size": "🔋",
}

OPTIONAL_FIELDS = ["battery_size"]
