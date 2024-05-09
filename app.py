from flask import Flask, render_template, request,url_for,jsonify
import os
from chest_cancer import chest







if __name__=='__main__':
    img_path = './adeno.png'
    print(chest(img_path))