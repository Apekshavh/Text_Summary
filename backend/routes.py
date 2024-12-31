from flask import Blueprint, request, jsonify
from summarizer import SummarizerService

def create_api_routes():
    api = Blueprint('api', __name__)
    summarizer = SummarizerService()

    @api.route('/summarize', methods=['POST'])
    def summarize():
        try:
            data = request.json
            input_text = data.get('text', '')
            summary = summarizer.generate_summary(input_text)
            return jsonify({'summary': summary})
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return api