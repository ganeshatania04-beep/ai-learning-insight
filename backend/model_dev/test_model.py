#!/usr/bin/env python3
"""
Test script to verify ML model files can be loaded
"""

import pickle
import os
import sys
import json

def test_model_files():
    """Test if all required model files can be loaded"""
    print("=" * 60)
    print("🧪 TESTING ML MODEL FILES")
    print("=" * 60)
    
    # Get current directory
    current_dir = os.getcwd()
    print(f"\n📁 Current Directory: {current_dir}\n")
    
    # List of files to check - DISESUAIKAN DENGAN FILE ANDA
    files_to_test = [
        'clustering_model.pkl',      # ← File ini ADA
        'predictor_model.pkl',       # ← File ini ADA
        'api_documentation.json',    # ← File ini ADA
        'model_metadata.json',       # ← File ini ADA
        'learning_patterns.json'     # ← File ini ADA
    ]
    
    results = []
    
    # Test each file
    for filename in files_to_test:
        print(f"Testing {filename}...")
        print("-" * 40)
        
        # Check if file exists
        if not os.path.exists(filename):
            print(f"  ❌ ERROR: {filename} NOT FOUND!")
            results.append((filename, False))
            print()
            continue
        
        try:
            if filename.endswith('.pkl'):
                # Test pickle files
                with open(filename, 'rb') as f:
                    model = pickle.load(f)
                print(f"  ✅ {filename} loaded successfully!")
                print(f"     Type: {type(model).__name__}")
                print(f"     Size: {os.path.getsize(filename) / 1024:.2f} KB")
                
            elif filename.endswith('.json'):
                # Test JSON files
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                print(f"  ✅ {filename} loaded successfully!")
                print(f"     Keys: {list(data.keys())}")
                print(f"     Size: {os.path.getsize(filename) / 1024:.2f} KB")
            
            results.append((filename, True))
            
        except Exception as e:
            print(f"  ❌ ERROR loading {filename}")
            print(f"     Error: {str(e)}")
            results.append((filename, False))
        
        print()
    
    # Summary
    print("=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    for filename, status in results:
        status_icon = "✅" if status else "❌"
        print(f"{status_icon} {filename}")
    
    success_count = sum(1 for _, status in results if status)
    total_count = len(results)
    
    print(f"\n{'✅' if success_count == total_count else '⚠️'} Results: {success_count}/{total_count} files loaded successfully")
    
    if success_count == total_count:
        print("\n🎉 ALL MODEL FILES LOADED SUCCESSFULLY!")
        print("✅ You are ready to proceed to backend integration!")
        return True
    else:
        print(f"\n⚠️ WARNING: {total_count - success_count} file(s) failed to load!")
        print("Please fix the issues before proceeding.")
        return False

def test_python_packages():
    """Test if required Python packages are installed"""
    print("=" * 60)
    print("🐍 TESTING PYTHON PACKAGES")
    print("=" * 60)
    print()
    
    required_packages = [
        ('numpy', 'numpy'),
        ('pandas', 'pandas'),
        ('sklearn', 'scikit-learn'),
        ('joblib', 'joblib'),
    ]
    
    all_installed = True
    
    for import_name, package_name in required_packages:
        try:
            module = __import__(import_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"✅ {package_name:20s} v{version}")
        except ImportError:
            print(f"❌ {package_name:20s} NOT INSTALLED")
            all_installed = False
    
    print()
    
    if all_installed:
        print("✅ All required packages are installed!\n")
    else:
        print("⚠️ Some packages are missing!")
        print("Run: pip install -r requirements.txt\n")
    
    return all_installed

def main():
    """Main function"""
    print("\n" + "=" * 60)
    print("🚀 AI LEARNING INSIGHT - MODEL VALIDATION")
    print("=" * 60)
    print()
    
    # Test Python packages
    packages_ok = test_python_packages()
    
    if not packages_ok:
        print("❌ FAILED: Please install required packages first!")
        print("   Command: pip install -r requirements.txt")
        return False
    
    # Test model files
    files_ok = test_model_files()
    
    if files_ok:
        print("\n" + "=" * 60)
        print("✅ VALIDATION COMPLETE - ALL TESTS PASSED!")
        print("=" * 60)
        print("\n🎯 Next Step: Proceed to backend integration")
        print("   Command: cd ../backend && npm start\n")
        return True
    else:
        print("\n" + "=" * 60)
        print("❌ VALIDATION FAILED")
        print("=" * 60)
        print("\nPlease fix the issues above before proceeding.\n")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)